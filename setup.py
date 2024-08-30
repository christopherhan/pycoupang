from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pycoupang",
    version="0.1.0",
    author="Chris Han",
    author_email="chris@blackarrow.software",
    description="A Python client for the Coupang API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pycoupang",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)