# To find available Node images, see https://mcr.microsoft.com/en-us/artifact/mar/devcontainers/python/tags

# [Choice] Python version
ARG VARIANT="3.11"
FROM mcr.microsoft.com/devcontainers/python:${VARIANT}

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    # Install additional packages
    git \
    # Install the Azure CLI
    && curl -sL https://aka.ms/InstallAzureCLIDeb | bash

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

COPY src/ /workspace/src/
COPY pyproject.toml /workspace/

RUN cd /workspace && poetry install

# Install the GitHub CLI see:
# https://github.com/microsoft/vscode-dev-containers/blob/3d59f9fe37edb68f78874620f33dac5a62ef2b93/script-library/docs/github.md
COPY library-scripts/github-debian.sh /tmp/library-scripts/
RUN apt-get update && bash /tmp/library-scripts/github-debian.sh
