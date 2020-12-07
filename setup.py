import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="uberfile-pkg",
    version="0.0.1",
    author="Shutdown en1ma",
    description="Uberfile is a simple command-line tool aimed to help pentesters quickly generate file downloader one-liners.",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ShutdownRepo/uberfile",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)




