# Enhance Your Codespace with GitHub Copilot

![Deprecation Badge](https://img.shields.io/badge/Skills-Deprecated-333?logo=github&labelColor=454c54&color=bf8700)

This repository provides a quick guide for adding GitHub Copilot to a
Codespace. The original skills exercise has been deprecated, so refer to
[Getting Started with GitHub Copilot](https://github.com/skills/getting-started-with-github-copilot)
for updated learning material.

## Overview

GitHub Copilot is an AI pair programmer that suggests complete lines or
functions as you type. The extension works in VS Code, Visual Studio,
JetBrains IDEs, and Neovim. Copilot is trained on public repositories
and adapts to many languages.

Running Copilot in a Codespace showcases GitHub's
[Collaborative Coding](https://github.com/features#features-collaboration)
tools. Before you begin, we recommend completing the
[Codespaces](https://github.com/skills/code-with-codespaces) skill.

## Set Up a Dev Container with Copilot

1. In your repository, create `.devcontainer/devcontainer.json`.
2. Add the following configuration:
   ```
   {
       // Name this configuration
       "name": "Codespace for Skills!",
       "customizations": {
           "vscode": {
               "extensions": [
                   "GitHub.copilot"
               ]
           }
       }
   }
   ```
3. Commit the new file to the `main` branch.

## Launch Your Codespace

1. Open the **Code** tab of your repository.
2. Click **Codespaces** and then **Create codespace on main**.
3. Wait a few minutes for the environment to build.
4. When the editor appears, confirm the Copilot extension is installed:
   ![Codespace screenshot one][img1]
   ![Codespace screenshot two][img2]

## Need Help?

Post in our [discussion board](https://github.com/orgs/skills/discussions/categories/code-with-copilot)
or check the [GitHub status page](https://www.githubstatus.com/).

## License and Conduct

This project is covered by the [MIT License](https://gh.io/mit). By
contributing, you agree to our
[Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md).

[img1]:
https://user-images.githubusercontent.com/26442605/224102962-d0222578-3f10-4566-856d-8d59f28fcf2e.png
[img2]:
https://user-images.githubusercontent.com/26442605/224102514-7d6d2f51-f435-401d-a529-7bae3ae3e511.png
