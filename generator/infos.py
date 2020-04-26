from generator.model.readme import ReadmeModel
from generator.utils import get_readme_json, create_json


def get_info_readme():
    data = get_readme_json()
    return ReadmeModel.from_json(data)


def create_info_json():
    readme = ReadmeModel(
        project_name=None,
        version=None,
        description=None,
        author=None,
        github_username=None,
        author_linkedin_username=None,
        author_twitter_username=None,
        author_website=None,
        homepage=None,
        project_demo_url=None,
        repository_url=None,
        contributing_url=None,
        documentation_url=None,
        license_url=None,
        issues_url=None,
        license=None,
        install_command=None,
        usage_command=None,
        test_command=None,
        repository=None,
        credits=None,
        is_github_repos=None,
        has_start_command=None,
        has_test_command=None
        )
    create_json(readme.to_json())

