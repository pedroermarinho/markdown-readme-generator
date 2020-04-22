import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='readme-generator',
    version='0.1.0',
    packages=setuptools.find_packages(),
    url='https://github.com/pedroermarinho/readme-generator',
    license='MIT',
    author='Pedro Marinho',
    author_email='pedro.marinho238@gmail.com',
    description='readme generator',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
