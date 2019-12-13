import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="QeezPy", # Replace with your own username
    version="0.0.3",
    author="Piotr Szewczyk",
    author_email="piotr.szewczyk96@gmail.com",
    description="Selenium WebDriver Python Framework to create POM tests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pszewczykpl/QeezPy",
    package_dir={"": "src"},
    packages=["qeezpy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8'
)
