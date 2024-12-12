import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__ = "0.0.0"

REPONAME = "Text-Sumarizer"
AUTHOR = "Moksha Wiyathunga"
SRC_REPO = "TextSumarizer"
AUTHOR_EMAIL = "mokshadil@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR}/{REPONAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR}/{REPONAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)