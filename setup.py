import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name='markdown-readme-generator',
    keywords='markdown readme mrgenerator generator',
    version='0.1.4',
    # 1.2.0.dev1  # Development release
    # 1.2.0a1     # Alpha Release
    # 1.2.0b1     # Beta Release
    # 1.2.0rc1    # Release Candidate
    # 1.2.0       # Final Release
    packages=setuptools.find_packages(),
    package_data={
        "": ["*.pmd"],
    },
    url='https://github.com/pedroermarinho/markdown-readme-generator',
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
    project_urls={
        'Documentation': 'https://github.com/pedroermarinho/markdown-readme-generator',
        'Say Thanks!': 'https://github.com/pedroermarinho/markdown-readme-generator',
        'Source': 'https://github.com/pedroermarinho/markdown-readme-generator',
        'Tracker': 'https://github.com/pedroermarinho/markdown-readme-generator/issues',
    },
    python_requires='~=3.6',
    install_requires=requirements,
    entry_points={'console_scripts': ['mrgenerator-cli = mrgenerator.run:cli']}
)
