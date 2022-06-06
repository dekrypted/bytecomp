from setuptools import setup, find_packages

setup(
    name="bytecomp",
    version="1.1.0",
    author="DeKrypt",
    author_email="gregcoolkidd@gmail.com",
    description="Utilities to work with bytecode.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dekrypted/bytecomp",
    project_urls={
        "Bug Tracker": "https://github.com/dekrypted/bytecomp/issues",
    },
    keywords=['bytecode','python']
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.5",
)
