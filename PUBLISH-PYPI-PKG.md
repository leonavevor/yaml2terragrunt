
# Publish Python Package to PyPi (using poetry)

ref: https://www.digitalocean.com/community/tutorials/how-to-publish-python-packages-to-pypi-using-poetry-on-ubuntu-22-04 (publish to pypi using poetry)
ref: https://python-poetry.org/docs/cli/ (using the published pypi package in your python project) (alternatively add from git or local path)

#### Tutorial

# How To Publish Python Packages to PyPI using Poetry on Ubuntu 22.04

Published on October 20, 2022

-   [Python](https://www.digitalocean.com/community/tags/python "Python")
-   [Ubuntu 22.04](https://www.digitalocean.com/community/tags/ubuntu-22-04 "Ubuntu 22.04")

![author](https://www.gravatar.com/avatar/9e398be78819dace9747161327c2638a6e1ec881e9bf4ed30df4d77133b0dc14?default=retro)

[Tony Tran](https://www.digitalocean.com/community/users/tonytran)

![How To Publish Python Packages to PyPI using Poetry on Ubuntu 22.04](https://www.digitalocean.com/api/static-content/v1/images?src=https%3A%2F%2Fcommunity-cdn-digitalocean-com.global.ssl.fastly.net%2FKZLf3p2xbGteFzvZRcfw4D9v&width=1920 "How To Publish Python Packages to PyPI using Poetry on Ubuntu 22.04")

### [Introduction](https://www.digitalocean.com/community/tutorials/how-to-publish-python-packages-to-pypi-using-poetry-on-ubuntu-22-04#introduction)[](https://www.digitalocean.com/community/tutorials/how-to-publish-python-packages-to-pypi-using-poetry-on-ubuntu-22-04#introduction)

[Poetry](https://python-poetry.org/) is a dependency manager for Python that is also capable of building and packaging your Python projects for distribution. [PyPI](https://pypi.org/) is the official Python repository for uploading and downloading Python packages, and will be used in this tutorial. It is the official third party source for Python packages, and is operated by the Python Software Foundation. Publishing your packages on PyPI makes it publicly available for installation by yourself, or anyone else.

In this tutorial you will create a PyPI account, set up token authentication with your account to enable use with Poetry, then build and publish your packaged project onto PyPI. This will also enable you to add your published package as a dependency to your other Python projects.

## [Prerequisites](https://www.digitalocean.com/community/tutorials/how-to-publish-python-packages-to-pypi-using-poetry-on-ubuntu-22-04#prerequisites)[](https://www.digitalocean.com/community/tutorials/how-to-publish-python-packages-to-pypi-using-poetry-on-ubuntu-22-04#prerequisites)

-   An Ubuntu 22.04 server, set up according to our [initial server setup guide for Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu), with a non-**root** user with `sudo` privileges and a firewall enabled.
-   The latest version of Python 3 installed on your machine following **Step 1** of [how to install Python 3 and set up a programming environment on an Ubuntu 22.04 server](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-22-04-server).
-   Poetry installed on your system, following this guide on [how to install Poetry to manage Python dependencies on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-install-poetry-to-manage-python-dependencies-on-ubuntu-22-04).

## [Step 1 — Creating a PyPI Account](https://www.digitalocean.com/community/tutorials/how-to-publish-python-packages-to-pypi-using-poetry-on-ubuntu-22-04#step-1-creating-a-pypi-account)[](https://www.digitalocean.com/community/tutorials/how-to-publish-python-packages-to-pypi-using-poetry-on-ubuntu-22-04#step-1-creating-a-pypi-account)

In order to publish a package to PyPI, you will need to create an account. Go to the [official registration page](https://pypi.org/account/register/) in your web browser:

![PyPI Signup Page](https://deved-images.nyc3.cdn.digitaloceanspaces.com/poetry-pypi/pypi-signup.png)

PyPI Signup Page

Next you will need to enable token authentication in order to safely use your PyPI credentials with Poetry.

## [Step 2 — Enabling Token Authentication for PyPI](https://www.digitalocean.com/community/tutorials/how-to-publish-python-packages-to-pypi-using-poetry-on-ubuntu-22-04#step-2-enabling-token-authentication-for-pypi)[](https://www.digitalocean.com/community/tutorials/how-to-publish-python-packages-to-pypi-using-poetry-on-ubuntu-22-04#step-2-enabling-token-authentication-for-pypi)

Token authentication is the recommended way to use your PyPI account in the command line. You can use a single, automatically generated token instead of a username and password. Tokens can be added and revoked at any time or granted granular access to parts of your account. This makes them more secure, and avoids the risk of your password being compromised. You will need to create a new API token for your account by navigating to your [account settings](https://pypi.org/manage/account/):

![PyPI Account Settings](https://deved-images.nyc3.cdn.digitaloceanspaces.com/poetry-pypi/pypi-account-settings.png)

PyPI Account Settings

Scroll down until you reach the **“API tokens”** section. Click on **“Add API token”**:

![PyPI Add API Token](https://deved-images.nyc3.cdn.digitaloceanspaces.com/poetry-pypi/pypi-api-tokens.png)

PyPI Add API Token

On the following page, you can name your token. This tutorial will name it `poetry`, but feel free to choose whatever name you’d like:

![PyPI API Token Creation](https://deved-images.nyc3.cdn.digitaloceanspaces.com/poetry-pypi/pypi-token-creation.png)

PyPI API Token Creation

Once your token is created, it is important to copy your token because it will only be shown once. This is common practice with API tokens that allow you to make a new one as needed, so make note of your token before proceeding.

![PyPI Copy Warning](https://deved-images.nyc3.cdn.digitaloceanspaces.com/poetry-pypi/pypi-token-appears-once-copy.png)

PyPI Copy Warning

You will now use this token to configure your credentials in Poetry to prepare for publishing. Instead of appending your API token to every command that needs it in Poetry, instead you will do it once using Poetry’s `config`command.

Add your API token to Poetry with this command:

```
<ol><li data-prefix="$">poetry config pypi-token.pypi <mark>your-api-token</mark>
</li></ol>
```

Copy

With your API token added as your credentials, Poetry will notify you that your credentials are stored in a plaintext file. This would be an issue if you were using a traditional username and password for your credentials. Given that tokens can be easily deleted and renewed, while also being randomly generated and unique to a single use case, this makes token storage here a safe trade off for convenience. Alternatively, you can opt to enter your API token manually for each command.

With this, you are ready to build and then publish your project.

## [Step 3 — Building your Project](https://www.digitalocean.com/community/tutorials/how-to-publish-python-packages-to-pypi-using-poetry-on-ubuntu-22-04#step-3-building-your-project)[](https://www.digitalocean.com/community/tutorials/how-to-publish-python-packages-to-pypi-using-poetry-on-ubuntu-22-04#step-3-building-your-project)

Building is the same as packaging your project, and this is a required step before you can publish it. To build your project, enter the following:

```
poetry build
```

Copy

```
<div class="secondary-code-label" title="Output">Output</div>Building sammy-poetry (0.1.0)
  - Building sdist
  - Built sammy-poetry-0.1.0.tar.gz
  - Building wheel
  - Built sammy_poetry-0.1.0-py3-none-any.whl
```

Two files will be outputted. First is the source which is `sdist`, that outputs to a `tar.gz` file. Second is the compiled package, which is `wheel`, that outputs to a `.whl` file. With these files, you are now ready to publish your Python package to PyPI.

## [Step 4 — Publishing your Python Package to PyPI](https://www.digitalocean.com/community/tutorials/how-to-publish-python-packages-to-pypi-using-poetry-on-ubuntu-22-04#step-4-publishing-your-python-package-to-pypi)[](https://www.digitalocean.com/community/tutorials/how-to-publish-python-packages-to-pypi-using-poetry-on-ubuntu-22-04#step-4-publishing-your-python-package-to-pypi)

PyPI is the default publishing target for Poetry. With your authentication API token already in place, your publish command will not need to include your credentials again.

To publish your compiled package, enter the following:

```
poetry publish
```

Copy

```
<div class="secondary-code-label" title="Output">Output</div>Publishing sammy-poetry (0.1.0) to PyPI
 - Uploading sammy-poetry-0.1.0.tar.gz 100%
 - Uploading sammy_poetry-0.1.0-py3-none-any.whl 100%
```

You can now check your published package. Open up [your PyPI projects](https://pypi.org/manage/projects/) in your browser.

![PyPI Your Uploaded Package](https://deved-images.nyc3.cdn.digitaloceanspaces.com/poetry-pypi/pypi-uploaded-sammy-poetry.png)

PyPI Your Uploaded Package

Your package is published, is publicly available on PyPI, and also available as a dependency through Poetry as well. You can add your own published package as a dependency in your other Python projects.

**Note:** You can build and publish your package to PyPI in one command by adding the following flag to your `publish` call:

```
<ol><li data-prefix="$">poetry publish <span class="token parameter variable">--build</span>
</li></ol>
```

Copy

This can be more efficient depending on the maturity of your project and workflow.

## [Conclusion](https://www.digitalocean.com/community/tutorials/how-to-publish-python-packages-to-pypi-using-poetry-on-ubuntu-22-04#conclusion)[](https://www.digitalocean.com/community/tutorials/how-to-publish-python-packages-to-pypi-using-poetry-on-ubuntu-22-04#conclusion)

In this tutorial, you have used Poetry for its building and publishing ability. You created a PyPI account, set up API Token authentication with Poetry, then compiled your project before publishing it. Your package is available as a dependency publicly, and can even be included as a dependency through Poetry.

Next, you may want to delve more deeply into Python by checking out our [How To Code in Python](https://www.digitalocean.com/community/tutorial-series/how-to-code-in-python-3) tutorial series.
