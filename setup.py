import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="HyTra", # Replace with your own username
    version="0.0.1",
    author="José Luis Balcázar",
    author_email="joseluisbalcazar@gmail.com",
    description="Hypergraph Transversals",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/balqui/HyTra",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
