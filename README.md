# Portfolio Website with MkDocs Material

This repository provides a template for creating a professional freelance portfolio website using MkDocs Material. Originally designed for technical documentation, MkDocs Material has evolved into a [powerful framework](https://squidfunk.github.io/mkdocs-material/blog/2024/08/19/how-were-transforming-material-for-mkdocs/) that's perfect for portfolios, blogs, and personal websites - all manageable through simple Markdown and YAML files.

## Why MkDocs Material?

- **Quick Setup**: Get your site running in minutes
- **Markdown-Based**: Write content in simple Markdown
- **Code-Friendly**: Built-in syntax highlighting and code blocks
- **Responsive Design**: Looks great on all devices
- **No Frontend Skills Needed**: Professional design out of the box
- **SEO Optimized**: Built-in SEO features
- **Search Functionality**: Full-text search included
- **Social Cards**: Auto-generated preview cards for social media sharing
- **Dark Mode**: Automatic dark/light theme switching

As you go through this setup, please find all the most up to date information in the [official documentation here](https://squidfunk.github.io/mkdocs-material/getting-started/).

## Continuous integration and deployment

The workflow in `.github/workflows/ci.yml` runs on pushes to any branch,
pull requests, and manual runs from the GitHub Actions tab. It uses Python
from `.python-version` and installs the dependencies in `requirements.txt`.
MkDocs and Material are pinned to the versions verified for this site;
transitive dependencies are resolved by pip.

The pipeline checks dependency compatibility and builds with `mkdocs build
--strict`, so configuration warnings and build errors fail the check. A
successful run saves the generated site as a `website` artifact for seven
days. Successful pushes or manual runs on the repository's default branch
also deploy to GitHub Pages. Other branches and pull requests only build.
Deployment uses the Pages URL supplied by GitHub, including repository
subpaths or a custom domain configured in Pages settings.

The website repository is
[jmallia91/mkdocs-website-jonathan](https://github.com/jmallia91/mkdocs-website-jonathan).
Push changes to its default branch to publish updates.
In **Settings > Pages > Build and deployment**, set **Source** to
**GitHub Actions** before running the deployment. Under **Actions**, check
the **Site CI and Pages** run. No personal access token is needed by the
workflow; it uses GitHub's built-in token. If you use
branch protection, select **Build MkDocs site** as a required check after its
first run.

Run the same checks locally in PowerShell:

```powershell
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -m mkdocs build --strict
```

## Quick Start

### Windows PowerShell (local preview)

With the project dependencies installed in `.venv`, run from this folder:

```powershell
.\.venv\Scripts\python.exe start_server.py
```

Open http://127.0.0.1:8000. Keep the terminal open; press Ctrl+C to stop.
Edit `docs/index.md` for the homepage and `mkdocs.yml` for the site settings.
The preview refreshes when you save changes.

For a fresh environment, use Python 3.11 or later:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

If the Python launcher cannot find Python and you have Anaconda installed,
replace the first command with:

```powershell
& "$env:USERPROFILE\anaconda3\python.exe" -m venv .venv
```

The preview launcher detects Cairo in the Python installation's `Library/bin`
folder (as supplied by Anaconda). Other installations may need the
[Windows image-processing dependencies](https://squidfunk.github.io/mkdocs-material/plugins/requirements/image-processing/).
If `.venv/windows-ca.pem` exists, the launcher uses it for HTTPS requests
unless `REQUESTS_CA_BUNDLE` is already set.


### Option 1: Local Installation (Recommended for Mac Users)

1. **Clone this repository**
   ```bash
   git clone https://github.com/datalumina/mkdocs-website-template.git
   cd mkdocs-website-template
   ```

2. **Install MkDocs Material**
   ```bash
   pip install "mkdocs-material[imaging]"
   
   # For MacOS, install required dependencies
   brew install cairo freetype libffi libjpeg libpng zlib pngquant
   ```

3. **Preview your site**
   ```bash
    # For MacOS M1/M2 users
    export DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib
    mkdocs serve
   ```
   Visit `http://localhost:8000` to see your site.

> **Note on Operating Systems**: 
> - This setup has been thoroughly tested on MacOS (Intel and Apple Silicon)
> - Windows setup instructions are still being updated
> - If you encounter any issues on Windows:
>   1. First, check the [official MkDocs Material documentation](https://squidfunk.github.io/mkdocs-material/getting-started/)
>   2. Try to resolve the issue using their troubleshooting guides
>   3. If the problem persists, please message Dave on Circle for assistance
>   4. Your feedback will help improve the documentation for other Windows users!


### Option 2: Using Docker (Recommended for Windows, Mac and Linux)

Docker provides a consistent environment across all operating systems, making it an excellent choice for development. This method works reliably on Windows, MacOS, and Linux.

-> Special thanks to our community member, Nisar, for contributing the Docker implementation! 🐳

1. **Download & Install Docker Desktop**
https://docs.docker.com/get-started/get-docker/

2. **Clone this repository**
   ```bash
   git clone https://github.com/data-freelancer-mastermind/mkdocs-website-template.git
   cd mkdocs-website-template
   ```

3. **Start the server**
   ```bash
   chmod +x start_server.sh
   ./start_server.sh
   ```
   Visit `http://localhost:8000` to see your site.

## Customizing Your Portfolio

### 1. Basic Configuration

Edit `mkdocs.yml` to customize your site:

- Site name and metadata
- Navigation structure
- Color scheme and fonts
- Custom CSS settings in `stylesheets/extra.css`
- Social links
- Extensions and plugins

### 2. Content Structure

```bash
docs/
├── index.md # Your homepage
├── about.md # About page
├── portfolio/ # Your work
├── blog/ # Blog posts
└── assets/ # Images and other files
```

## Deployment

I recommend publishing your site with GitHub Pages. If you want to keep your repo private, you need a GitHub Pro subscription. Public repos can be deployed with a free GitHub account.

1. Push your repository to GitHub
2. Follow the instructions here: [Publishing your site](https://squidfunk.github.io/mkdocs-material/publishing-your-site/)
3. Set up the GitHub actions for your project
4. Test the deployment by pushing changes

### Custom Domain



1. Add a `CNAME` file in your `docs` folder with your domain
2. Go to `repository/settings/pages` and check the domain settings
3. Follow the [instructions here](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site) to configure your domain and DNS settings
4. GitHub recently changed the DNS linking process: Let me know if we need to update these docs!
5. Also enable HTTPS on this page

## Useful Resources

- [Official MkDocs Material Documentation](https://squidfunk.github.io/mkdocs-material/getting-started/)
- [Icons and Emojis Reference](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/)
- [Blog Setup Guide](https://squidfunk.github.io/mkdocs-material/blog/)
- [Social Cards Configuration](https://squidfunk.github.io/mkdocs-material/plugins/requirements/image-processing/)
