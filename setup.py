import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="customlogging",
    version="0.0.6",
    author="Rishi Latchmepersad",
    author_email="latchmepersad@gmail.com",
    description="A logging package that allows logging to STDOUT, log files as well as SMTP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rishil321/customlogging",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
