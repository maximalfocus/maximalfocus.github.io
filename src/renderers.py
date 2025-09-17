from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from urllib.parse import quote_plus
from src.models import Post, Tag
from src.paginator import Paginator


def safe_urlencode(value):
    """A Jinja2 filter that URL-encodes a string, handling None safely."""
    if value is None:
        return ""
    return quote_plus(str(value))


class Renderer:
    def __init__(self, template_dir: Path):
        self.env = Environment(loader=FileSystemLoader(template_dir))
        self.env.filters["urlencode"] = safe_urlencode

    def render_post(self, post: Post, site_url: str, output_dir: Path):
        """Renders a single post to an HTML file inside its own directory."""
        template = self.env.get_template("post.html")
        rendered_html = template.render(post=post, site_url=site_url)

        # Create the post's directory, e.g., output/posts/post-slug/
        post_dir = output_dir / "posts" / post.slug
        post_dir.mkdir(parents=True, exist_ok=True)

        # Write the content to index.html within that directory
        output_file = post_dir / "index.html"
        output_file.write_text(rendered_html)

    def render_paginated_index(self, paginator: Paginator, output_dir: Path):
        """Renders all paginated index pages."""
        template = self.env.get_template("index.html")

        for page_data in paginator:
            page_num = page_data["page_num"]

            # Determine the output path
            if page_num == 1:
                page_dir = output_dir
            else:
                page_dir = output_dir / "page" / str(page_num)

            page_dir.mkdir(parents=True, exist_ok=True)
            output_file = page_dir / "index.html"

            rendered_html = template.render(page=page_data)
            output_file.write_text(rendered_html)

    def render_tag(self, tag: Tag, output_dir: Path):
        output_dir_tag = output_dir / "tags"
        output_dir_tag.mkdir(exist_ok=True)
        template = self.env.get_template("tag.html")
        title = f"Posts tagged: {tag.name}"
        rendered_html = template.render(posts=tag.posts, title=title)
        output_file = output_dir_tag / f"{tag.slug}.html"
        output_file.write_text(rendered_html)

    def render_diagram_tag(self, tag: Tag, output_dir: Path):
        """Renders the index page for a single diagram tag."""
        # The output path is now inside the /diagrams/tags/ directory
        output_dir_tag = output_dir / "diagrams" / "tags"
        output_dir_tag.mkdir(parents=True, exist_ok=True)

        template = self.env.get_template("tag.html")
        title = f"Diagrams tagged: {tag.name}"

        rendered_html = template.render(posts=tag.posts, title=title)
        output_file = output_dir_tag / f"{tag.slug}.html"
        output_file.write_text(rendered_html)

    def render_sitemap(self, posts: list[Post], site_url: str, output_dir: Path):
        """Renders the sitemap.xml file."""
        template = self.env.get_template("sitemap.xml")
        rendered_xml = template.render(posts=posts, site_url=site_url)

        output_file = output_dir / "sitemap.xml"
        output_file.write_text(rendered_xml)

    def render_rss(
        self,
        posts: list[Post],
        site_title: str,
        site_description: str,
        site_url: str,
        output_dir: Path,
        limit: int,
    ):
        """Renders the rss.xml file."""
        template = self.env.get_template("rss.xml")
        rendered_xml = template.render(
            posts=posts,
            site_title=site_title,
            site_description=site_description,
            site_url=site_url,
            limit=limit,
        )

        output_file = output_dir / "rss.xml"
        output_file.write_text(rendered_xml)

    def render_page(self, page: Post, output_dir: Path):
        """Renders a standalone page, allowing for a custom template."""
        template_name = page.template or "page.html"
        template = self.env.get_template(template_name)

        rendered_html = template.render(page=page)
        page_dir = output_dir / page.slug
        page_dir.mkdir(parents=True, exist_ok=True)
        output_file = page_dir / "index.html"
        output_file.write_text(rendered_html)

    def render_paginated_diagrams_index(self, paginator: Paginator, output_dir: Path):
        """Renders all paginated index pages for diagrams."""
        template = self.env.get_template("diagrams.html")
        title = "Diagrams"

        for page_data in paginator:
            page_num = page_data["page_num"]

            # Determine the output path (e.g., /diagrams/ or /diagrams/page/2/)
            if page_num == 1:
                page_dir = output_dir / "diagrams"
            else:
                page_dir = output_dir / "diagrams" / "page" / str(page_num)

            page_dir.mkdir(parents=True, exist_ok=True)
            output_file = page_dir / "index.html"

            rendered_html = template.render(page=page_data, title=title)
            output_file.write_text(rendered_html)

    def render_diagrams_rss(
        self,
        diagrams: list[Post],
        site_title: str,
        site_url: str,
        output_dir: Path,
        limit: int,
    ):
        """Renders the rss.xml file specifically for diagrams."""
        diagrams_dir = output_dir / "diagrams"
        diagrams_dir.mkdir(exist_ok=True)

        template = self.env.get_template("rss.xml")

        feed_title = f"Diagrams - {site_title}"
        feed_description = "A feed of the latest diagrams and visual explanations."

        rendered_xml = template.render(
            posts=diagrams,
            site_title=feed_title,
            site_description=feed_description,
            site_url=site_url,
            limit=limit,
        )

        output_file = diagrams_dir / "rss.xml"
        output_file.write_text(rendered_xml)
