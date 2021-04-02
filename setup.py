import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent


README = (HERE / "readme.md").read_text()


setup(
    name="moneycontrol",
    version="1.0.1",
    description="Web scraper for moneycontrol.com",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Avchhikara/moneycontrol",
    author="Avnish",
    author_email="avnishchhikara@outlook.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    keywords=[
        "moneycontrol",
        "money control",
        "web scraping",
        "scrape articles",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["requests", "beautifulsoup4"],
    entry_points={
        "console_scripts": [
            "moneycontrol=moneycontrol.__main__:main"
        ]
    },
)
