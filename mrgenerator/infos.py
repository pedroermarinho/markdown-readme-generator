from mrgenerator.model.readme import ReadmeModel
from mrgenerator.utils import get_readme_json, create_json


def get_info_readme():
    data = get_readme_json()
    return ReadmeModel.from_json(data)


def create_info_json():
    readme = ReadmeModel(
        project_name="new project",
        version="0.0.1",
        description="new project",
        author="your name",
        snap_store_name=None,
        icon_src=None,
        screenshot_src=None,
        github_username=None,
        author_linkedin_username=None,
        author_twitter_username=None,
        author_website=None,
        homepage="https://github.com/pedroermarinho/markdown-readme-generator#readme",
        project_demo_url="https://github.com/pedroermarinho/markdown-readme-generator#readme",
        repository_url="https://github.com/pedroermarinho/markdown-readme-generator",
        contributing_url="https://github.com/pedroermarinho/markdown-readme-generator/blob/master/CONTRIBUTING.md",
        documentation_url="https://github.com/pedroermarinho/markdown-readme-generator#readme",
        license_url="https://github.com/pedroermarinho/markdown-readme-generator/blob/master/LICENSE",
        issues_url="https://github.com/pedroermarinho/markdown-readme-generator/issues",
        license="MIT",
        install_command=["pip3 install markdown-readme-generator"],
        usage_command=["mrgenerator-cli"],
        test_command=["python3 run.py"],
        repository={
                    "type": "git",
                    "url": "git@github.com:pedroermarinho/markdown-readme-generator.git"
                    },
        credits=[
                    {
                      "name": "Markdown Readme Generator",
                      "url": "https://github.com/pedroermarinho/markdown-readme-generator"
                    }
                ],
        is_github_repos=True,
        has_start_command=True,
        has_test_command=True
        )
    create_json(readme.to_json())

