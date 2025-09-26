# Dockerfile

# ==========================================================================
# Stage 1: Build the Static Site
# ==========================================================================
# Pinning to a specific digest ensures 100% reproducible builds.
FROM ghcr.io/astral-sh/uv@sha256:00e6df6b8c046a1b447c5fb166d067e7efa29a60843db5faf2ea5907cacedc5c AS build

LABEL maintainer="Zhu Weijie"
LABEL description="Build stage for the static site generator."

WORKDIR /app

# --- Layer 1: Python Dependencies (changes rarely) ---
# By copying only this file first, the subsequent `uv run` step will be able to
# cache the dependency installation part of its process.
COPY pyproject.toml .

# --- Layer 2: Application Code (changes occasionally) ---
# Your core logic, templates, and static assets change less often than content.
COPY src ./src
COPY templates ./templates
COPY static ./static
COPY pages ./pages

# --- Layer 3: Content (changes frequently) ---
# Your markdown files are the most frequently changed part of the project.
# By placing this last, we ensure that changes here only invalidate this final
# build step, while all the layers above remain cached.
COPY content ./content

# --- Final Step: Install Python and Run the Build ---
# We combine these into a single layer. `uv run` is highly efficient. When it runs,
# it will see that the `pyproject.toml` file (from the cached layer) has not changed,
# so the dependency resolution part will be extremely fast.
RUN uv python install 3.12 && uv run python -m src.main


# ==========================================================================
# Stage 2: Serve the Site with Caddy
# ==========================================================================
FROM caddy@sha256:a4180db0805b3725ddf936d2e6290553745c7339c003565da717ee612fd8a888

LABEL maintainer="Zhu Weijie"
LABEL description="Production stage. Serves the static site with Caddy."

COPY --from=build /app/output /srv/
COPY Caddyfile /etc/caddy/Caddyfile
