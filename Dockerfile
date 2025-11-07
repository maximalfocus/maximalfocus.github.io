# Dockerfile

# ==========================================================================
# Stage 1: Build the Static Site
# ==========================================================================
# Pinning to a specific digest ensures 100% reproducible builds.
FROM ghcr.io/astral-sh/uv@sha256:00e6df6b8c046a1b447c5fb166d067e7efa29a60843db5faf2ea5907cacedc5c AS build

LABEL maintainer="Zhu Weijie"
LABEL description="Build stage for the static site generator."

WORKDIR /app

# --- Install Python FIRST (changes rarely) ---
RUN uv python install 3.14

# --- Layer 1: Python Dependencies (changes rarely) ---
COPY pyproject.toml .

# Pre-install dependencies without lock file
RUN uv sync --no-dev

# --- Layer 2: Application Code (changes occasionally) ---
COPY src ./src
COPY templates ./templates
COPY static ./static
COPY pages ./pages

# --- Layer 3: Content (changes frequently) ---
COPY content ./content

# --- Final Step: Run the Build ---
RUN uv run python -m src.main


# ==========================================================================
# Stage 2: Serve the Site with Caddy
# ==========================================================================
FROM caddy@sha256:a4180db0805b3725ddf936d2e6290553745c7339c003565da717ee612fd8a888

LABEL maintainer="Zhu Weijie"
LABEL description="Production stage. Serves the static site with Caddy."

COPY --from=build /app/output /srv/
COPY Caddyfile /etc/caddy/Caddyfile
