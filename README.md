# Contributing to <i>womeninoss.com</i>
This tutorial will guide you through setting up the *Women in Open Source* website locally using Jekyll. As a contributor, you'll need to clone the repository, make changes, and test them before submitting your contributions.  

## Prerequisites  

Ensure you have the following installed:  
- **Ruby** (3.0 or later recommended)  
- **RubyGems** (comes with Ruby)  
- **Bundler** (Ruby dependency manager)  
- **Git**  

### Installing Ruby and Bundler  

For Linux/macOS, install Ruby using a package manager:  

```sh
# macOS (using Homebrew)
brew install ruby

# Ubuntu/Debian
sudo apt update && sudo apt install ruby-full build-essential zlib1g-dev
```

For Windows, install [RubyInstaller](https://rubyinstaller.org/) and ensure you check the option to add Ruby to the system PATH.  

After installing Ruby, install Bundler:  

```sh
gem install bundler
```

## Cloning the Repository  

Fork and clone the *Women in Open Source* repository from GitHub:  

```sh
git clone https://github.com/lsurobotics/womeninoss.git
cd womeninoss
```

## Installing Dependencies  

The project uses Bundler to manage dependencies. Inside the repository folder, run:  

```sh
bundle install
```

This installs all required gems, including Jekyll and any theme dependencies.  

## Running the Site Locally  

Start the Jekyll server with:  

```sh
bundle exec jekyll serve
```

This will:  
- Build the site  
- Start a local development server at `http://127.0.0.1:4000`  

Open this URL in a browser to preview your changes. 

## Files and Folders
| Folder/File   | Purpose  |  
|--------------|----------------------------------------------------|  
| `js/`        | Contains JavaScript files for site functionality and interactivity. |  
| `css/`       | Holds stylesheets that define the website’s design and layout. |  
| `_posts/`    | Stores Markdown files for discussion posts, following Jekyll’s post format. |  
| `_layouts/`  | Contains HTML templates that structure different types of pages. |  
| `_site/`     | Automatically generated static site files (**do not edit, will be overwritten**). |  
| `_config.yml` | Defines site-wide settings, including metadata, plugins, and configurations. |  
| `index.html` | The main homepage file that determines the front page content and layout. |  
| `img/`       | Stores image assets used throughout the website. |

## Making Changes  

Modify the necessary files (e.g., posts, pages, styles). If you add a new page, update the `_config.yml` file if necessary.  

### Committing Your Changes  

After making edits, commit and push your changes:  

```sh
git add .
git commit -m "Describe your changes"
git push origin your-branch-name
```

Then, open a pull request on GitHub.  

## Additional Tips  

- If you run into issues, ensure your Ruby and Jekyll versions match the project's `.ruby-version` (if provided).  
- Use `bundle exec jekyll build` to generate the static site in `_site/`.  
- Follow any contribution guidelines outlined in the repository.  

Now you're ready to contribute to *Women in Open Source*! 🚀
