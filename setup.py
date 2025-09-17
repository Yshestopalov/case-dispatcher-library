from setuptools import setup, find_packages

setup(
    name="case_dispatcher",
    version="1.0.0",
    packages=find_packages(),
    description="A lightweight Python library for cleaning up chained if-else statements.",
    author="Yurii Shestopalov",
    author_email="yurii.shestopalov@gmail.com",
    url="https://github.com/Yshestopalov/case-dispatcher-library",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: Other/Proprietary License",
    ],
    python_requires=">=3.7",
)
