import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="HyTra", 
    version="0.0.3a1",
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
        "Development Status :: 3 - Alpha",
        "Topic :: Scientific/Engineering :: Mathematics"
    ],
    python_requires='>=2.7',
)
