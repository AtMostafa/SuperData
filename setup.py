import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="superdata", # Replace with your own username
    version="0.1.1",
    author="Mostafa",
    author_email="EmailAtMostafa@gmail.com",
    description="A super package that imports datascience packages to the namespace",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/atmostafa/superdata",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    install_requires=[
        'numpy',
        'matplotlib',
        'pandas'
    ]
)