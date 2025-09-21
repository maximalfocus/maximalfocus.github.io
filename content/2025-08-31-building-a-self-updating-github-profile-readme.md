---
title: "Building a Self-Updating GitHub Profile README"
date: 2025-08-31
type: post
tags:
  - github
  - automation
---

I was inspired by Simon Willison on this feature and decided to build my own version. My profile now automatically displays my latest blog posts and my most recently updated GitHub projects, ensuring it's always current without manual work.

This post explains exactly how it works.

#### The Three Core Components

The whole system is surprisingly simple and relies on three parts working together:

1.  **A `README.md` Template:** The README file acts as a template with special placeholders.
2.  **A Python Script:** A script that fetches the latest data from my blog and GitHub.
3.  **A GitHub Actions Workflow:** The automation engine that runs the script on a schedule.

#### 1. The `README.md` Template

The core of my README looks like this, using an HTML `<table>` to create a two-column layout:

```markdown
<table>
<tr>
<td valign="top" width="50%">

### Recent Projects
<!-- recent_projects starts -->
<!-- recent_projects ends -->

</td>
<td valign="top" width="50%">

### On My Blog
<!-- blog starts -->
<!-- blog ends -->

</td>
</tr>
</table>
```

The script looks for these `<!-- marker starts -->` and `<!-- marker ends -->` comments and replaces everything between them with freshly generated content.

#### 2. The Python Script (`build_readme.py`)

The Python script is responsible for two main tasks: fetching my recent projects and fetching my latest blog posts.

**Fetching Recent Projects**

To get my latest projects, the script makes an authenticated call to the GitHub REST API.

*   It hits the endpoint `https://api.github.com/users/zhu-weijie/repos`.
*   It uses query parameters `?sort=pushed&direction=desc` to get the repositories I've most recently pushed updates to.
*   The result is formatted into a clean Markdown list, including each project's description.

**Fetching Blog Posts**

My blog generates an `rss.xml` file, which is a standard feed format. The script uses the `feedparser` library to read and parse this feed.

It simply fetches the content from `https://zhu-weijie.github.io/rss.xml`, takes the 17 most recent entries, and formats them into a Markdown list with links to each post.

Once both lists are generated, the script reads the `README.md`, uses a simple regular expression to replace the content within the placeholder comments, and writes the file back to disk.

#### 3. The Automation: GitHub Actions

The workflow is configured to run on three triggers:

*   **`on: push`**: Every time I push a change to the `main` branch.
*   **`on: schedule`**: On a timer, currently set to run every two hours.
*   **`on: workflow_dispatch`**: A manual trigger, so I can run it from the Actions tab whenever I want.

The workflow itself has a sequence of simple steps:

1.  **Check out repo:** It checks out the latest version of the repository's code.
2.  **Set up Python:** It installs my desired Python version (3.12).
3.  **Install dependencies:** It runs `pip install -r requirements.txt`.
4.  **Update README:** It executes the `build_readme.py` script. Crucially, it passes the `secrets.GITHUB_TOKEN` to the script as an environment variable, which is used for the authenticated API call.
5.  **Commit and push if changed:** It checks if the `README.md` file has been modified.
    *   If it has, the workflow commits the changes with a standard message ("Updated README content") and pushes them back to the repository.
    *   If there are no changes, the commit command fails, but `|| exit 0` tells the workflow to continue and exit successfully, preventing unnecessary "failed" runs.

And that's it! You can find the full source code for this project in [this repository](https://github.com/zhu-weijie/zhu-weijie).
