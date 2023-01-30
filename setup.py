import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="pipedrive-python-lib",
    version="1.2.1",
    description="API wrapper for Pipedrive written in Python",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/GearPlug/pipedrive-python",
    author="Miguel Ferrer",
    author_email="ingferrermiguel@gmail.com",
    license="MIT",
    packages=["pipedrive"],
    install_requires=[
        "requests",
    ],
    zip_safe=False,
)
