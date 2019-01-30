import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="buckle-up",
    version="0.0.4",
    author="Mark Wadham",
    author_email="buckle-up@rkw.io",
    description="Buckle-up: a toolbox for writing macOS sandbox profiles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/m4rkw/buckle-up",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts = ["bu"],
)
