# DevOps CI/CD Demo

A small Flask web app packaged with Docker. GitHub Actions runs the tests and builds the image for pushes and pull requests. When you create a version tag, it can also publish the image to Docker Hub (after you add the two repository secrets).

## What the pipeline does

1. Checks out the repository and installs Python dependencies.
2. Runs two checks: the home page responds and `/health` returns `{"status":"ok"}`.
3. Builds a Docker image after the checks pass.
4. On a `v*` tag, publishes the image to Docker Hub if Docker Hub credentials are configured.

## Run locally

Install Python 3.12 or newer, then from this folder:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -q
python -m app.main
```

Open <http://localhost:5000> and <http://localhost:5000/health>.

## Run with Docker

Install Docker Desktop, then run:

```powershell
docker compose up --build
```

Visit <http://localhost:5000>. Stop it with `Ctrl+C`; run `docker compose down` to remove the container.

## Put it on GitHub

1. Create a new empty GitHub repository named `devops-cicd-demo`.
2. In this folder, initialize Git, commit the files, add your repository as `origin`, and push the `main` branch. GitHub Actions will run automatically.
3. Open the repository's **Actions** tab and inspect the test and build jobs.

## Optional Docker Hub publishing

Create a Docker Hub access token. In the GitHub repository, open **Settings → Secrets and variables → Actions** and add:

- `DOCKERHUB_USERNAME`: your Docker Hub username
- `DOCKERHUB_TOKEN`: the access token (keep it private)

Then create and push a version tag:3

```powershell
git tag v1.0.0
git push origin v1.0.0
```

The publish job uploads `YOUR_USERNAME/devops-cicd-demo:v1.0.0`. The token is only read by GitHub Actions; do not put it in source files.

## Deploy the published image locally

After the publish job succeeds, replace `YOUR_USERNAME` below:

```powershell
docker run --rm -p 5000:5000 YOUR_USERNAME/devops-cicd-demo:v1.0.0
```

Open <http://localhost:5000>. This is the local deployment demonstration; GitHub-hosted runners cannot deploy directly to your personal computer.

## Project report outline (keep the final PDF to 1–2 pages)

- **Introduction:** A simple web app delivered through an automated CI/CD workflow.
- **Abstract:** GitHub Actions checks the app and builds a Docker image; a version tag can publish it to Docker Hub for local deployment.
- **Tools used:** Python, Flask, pytest, Docker, GitHub Actions, and optionally Docker Hub.
- **Steps:** Build the app and health endpoint; add checks; package it; configure CI; publish a tagged image; run the image locally.
- **Conclusion:** Automated checks and repeatable packaging make releases easier to validate and deploy.

## Evidence to collect for submission

- Screenshot of a successful GitHub Actions run showing the test and build jobs.
- Screenshot of the app running at `localhost:5000` and its `/health` response.
- If using Docker Hub, a screenshot showing the `v1.0.0` image tag.
- The repository URL and a short explanation of each workflow stage.

## Troubleshooting

- If port 5000 is already in use, change the left side of the Compose mapping to `5001:5000` and open `localhost:5001`.
- If PowerShell blocks virtual environment activation, run `python -m pip install -r requirements.txt` without activating it, or use Command Prompt's `.venv\Scripts\activate.bat`.
- If the Docker Hub publish job is skipped, check that both repository secrets exist and that the pushed tag begins with `v`.
