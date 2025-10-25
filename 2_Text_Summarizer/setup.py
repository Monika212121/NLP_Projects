import setuptools

with open("README.md", "r", encoding = "utf-8") as f:               # refer NOTE.md(3)
    my_long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "NLP_Projects"
AUTHOR_USER_NAME = "Monika212121"
SRC_REPO = "TextSummarizer"                                         # local package we created inside src folder
AUTHOR_EMAIL = "mgadewar12@gmail.com"

setuptools.setup(                                                   # refer NOTE.md(4)
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package for NLP app",
    long_description = my_long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages = setuptools.find_packages(where = "src")
)