from setuptools import setup, find_packages

setup(
    name="autochartpy",
    version="0.1.0",
    author="Abdul Saboor",
    author_email="abdulsaboor1994@gmail.com",
    description="Automatically generate charts and dashboards from datasets",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/abdulsaboorpk/autochartpy",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "plotly",
        "pytest",
        "kaleido"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)