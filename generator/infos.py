from generator.model.readme import ReadmeModel
from generator.utils import get_readme_json


def get_info_readme():
    data = get_readme_json()
    return ReadmeModel(
        project_name=data.get("project_name", None),
        version=data.get("version", None),
        description=data.get("description", None),
        author=data.get("author", None),
        github_username=data.get("github_username", None),
        author_linkedin_username=data.get("author_linkedin_username", None),
        author_twitter_username=data.get("author_twitter_username", None),
        author_website=data.get("author_website", None),
        homepage=data.get("homepage", None),
        project_demo_url=data.get("project_demo_url", None),
        repository_url=data.get("repository_url", None),
        contributing_url=data.get("contributing_url", None),
        documentation_url=data.get("documentation_url", None),
        license_url=data.get("license_url", None),
        issues_url=data.get("issues_url", None),
        license=data.get("license", None),
        install_command=data.get("install_command", None),
        usage_command=data.get("usage_command", None),
        test_command=data.get("test_command", None),
        repository=data.get("repository", None),
        credits=data.get("credits", None),
        is_github_repos=data.get("is_github_repos", None),
        has_start_command=data.get("has_start_command", None),
        has_test_command=data.get("has_test_command", None)
    )
