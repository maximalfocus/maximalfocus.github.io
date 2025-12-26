import shutil
import json
from bs4 import BeautifulSoup
from pathlib import Path
from collections import defaultdict
from src.parsers import parse_markdown_file
from src.renderers import Renderer
from src.models import Post, Tag
from src.paginator import Paginator


class SiteBuilder:
    def __init__(self):
        self.content_dir = Path("content")
        self.output_dir = Path("output")
        self.renderer = Renderer(Path("templates"))
        self.site_title = "Weijie Explains"
        self.site_description = "A blog about technology and web development."
        self.pages_dir = Path("pages")
        self.site_url = "https://maximalfocus.github.io"
        self.static_dir = Path("static")
        self.posts_per_page = 50
        self.diagrams_per_page = 50
        self.rss_feed_limit = 20

    def build(self):
        print("Starting site build...")

        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(exist_ok=True)

        if self.static_dir.exists():
            shutil.copytree(self.static_dir, self.output_dir / "static")
            print("Copied static files.")

        # 1. First, parse ALL markdown content from all source directories
        all_content = [parse_markdown_file(fp) for fp in self.content_dir.glob("**/*.md")]
        pages = [parse_markdown_file(fp) for fp in self.pages_dir.glob("*.md")]

        # 2. Next, filter the content into different types
        posts = sorted(
            [p for p in all_content if p.type == "post"],
            key=lambda p: p.date,
            reverse=True,
        )
        diagrams = sorted(
            [p for p in all_content if p.type == "diagram"],
            key=lambda p: p.date,
            reverse=True,
        )

        print(f"Found and parsed {len(posts)} posts.")
        print(f"Found and parsed {len(diagrams)} diagrams.")
        print(f"Found and parsed {len(pages)} standalone pages.")

        # 3. Related content, tag collection and rendering
        self._calculate_related_content(posts)
        self._calculate_related_content(diagrams)
        print("Calculated related content for all types.")

        post_tags = self._collect_tags(posts)
        diagram_tags = self._collect_tags(diagrams)
        print(
            f"Collected {len(post_tags)} tags for posts and {len(diagram_tags)} tags for diagrams."
        )

        # Render pages and posts (now includes diagrams as they are also 'Post' objects)
        for page in pages:
            self.renderer.render_page(page, self.output_dir)
        for item in all_content:
            self.renderer.render_post(item, self.site_url, self.output_dir)
        print("Rendered individual content pages.")

        # Tag pages are still based on 'posts'
        for tag in post_tags.values():
            self.renderer.render_tag(tag, self.output_dir)
        print(f"Rendered {len(post_tags)} post tag pages.")

        for tag in diagram_tags.values():
            self.renderer.render_diagram_tag(tag, self.output_dir)
        print(f"Rendered {len(diagram_tags)} diagram tag pages.")

        diagrams_paginator = Paginator(diagrams, self.diagrams_per_page)
        self.renderer.render_paginated_diagrams_index(
            diagrams_paginator, self.output_dir
        )
        print(f"Rendered {diagrams_paginator.total_pages} diagrams index pages.")

        # The main index and feeds are still based on 'posts'
        paginator = Paginator(posts, self.posts_per_page)
        self.renderer.render_paginated_index(paginator, self.output_dir)
        print(f"Rendered {paginator.total_pages} main index pages.")

        self.renderer.render_sitemap(posts, self.site_url, self.output_dir)
        self.renderer.render_rss(
            posts=posts,
            site_title=self.site_title,
            site_description=self.site_description,
            site_url=self.site_url,
            output_dir=self.output_dir,
            limit=self.rss_feed_limit,
        )
        print("Rendered sitemap and RSS feed for posts.")

        self.renderer.render_diagrams_rss(
            diagrams=diagrams,
            site_title=self.site_title,
            site_url=self.site_url,
            output_dir=self.output_dir,
            limit=self.rss_feed_limit,
        )
        print("Rendered RSS feed for diagrams.")

        # The search index should include EVERYTHING
        self._generate_search_index(all_content)
        print("Generated global search index.")

        print("Site build finished successfully.")

    def _generate_search_index(self, posts: list[Post]):
        """Generates a JSON search index from all posts."""
        search_data = []
        for post in posts:
            # Combine title, tags, and content into one string
            tags_text = " ".join(post.tags)

            soup = BeautifulSoup(post.content_html, "html.parser")
            plain_text_content = soup.get_text()

            # The final searchable content
            searchable_content = f"{post.title} {tags_text} {plain_text_content}"

            search_data.append(
                {
                    "title": post.title,
                    "url": post.permalink,
                    "content": searchable_content,
                }
            )

        output_file = self.output_dir / "search-index.json"
        output_file.write_text(json.dumps(search_data, indent=2))

    def _calculate_related_content(
        self, content_items: list[Post], max_related: int = 3
    ):
        """Calculates related content based on shared tags for a given list of items."""
        post_map = {p.slug: p for p in content_items}

        tag_map = defaultdict(list)
        for post in content_items:
            for tag in post.tags:
                tag_map[tag].append(post)

        for post in content_items:
            scores = defaultdict(int)
            for tag in post.tags:
                for related_post in tag_map[tag]:
                    if related_post.slug != post.slug:
                        scores[related_post.slug] += 1

            sorted_related_slugs = sorted(scores, key=scores.get, reverse=True)

            post.related_posts = [
                post_map[slug] for slug in sorted_related_slugs[:max_related]
            ]

    def _collect_tags(self, content_items: list[Post]) -> dict[str, Tag]:
        tags = defaultdict(lambda: Tag(name=""))
        for item in content_items:
            for tag_name in item.tags:
                if not tags[tag_name].name:
                    tags[tag_name].name = tag_name
                tags[tag_name].posts.append(item)
        return tags
