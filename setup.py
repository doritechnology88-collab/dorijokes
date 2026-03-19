from setuptools import setup, find_packages

setup(
    name="dorijokes",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Dori Empire",
    description="A fun Python jokes library with 100+ hilarious jokes 😂",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/dorijokes",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)