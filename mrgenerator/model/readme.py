class ReadmeModel:
    def __init__(self,
                 project_name: str =None,
                 version: str =None,
                 description: str=None,
                 snap_store_name: str=None,
                 icon_src: str=None,
                 screenshot_src: dict=None,
                 author: str=None,
                 github_username: str=None,
                 author_website: str=None,
                 author_linkedin_username: str=None,
                 author_twitter_username: str=None,
                 homepage: str=None,
                 project_demo_url: str=None,
                 repository_url: str=None,
                 contributing_url: str=None,
                 documentation_url: str=None,
                 license_url: str=None,
                 issues_url: str=None,
                 license: str=None,
                 install_command: list=None,
                 usage_command: list=None,
                 test_command: list=None,
                 repository: dict=None,
                 credits: list=None,
                 is_github_repos: bool=None,
                 has_start_command: bool=None,
                 has_test_command: bool=None
                 ):
        self.project_name = project_name
        self.version = version
        self.description = description
        self.snap_store_name = snap_store_name
        self.icon_src = icon_src
        self.screenshot_src = screenshot_src
        self.author = author
        self.github_username = github_username
        self.author_linkedin_username = author_linkedin_username
        self.author_twitter_username = author_twitter_username
        self.author_website = author_website
        self.homepage = homepage
        self.project_demo_url = project_demo_url
        self.repository_url = repository_url
        self.contributing_url = contributing_url
        self.documentation_url = documentation_url
        self.license_url = license_url
        self.issues_url = issues_url
        self.license = license
        self.install_command = install_command
        self.usage_command = usage_command
        self.test_command = test_command
        self.repository = repository
        self.credits = credits
        self.is_github_repos = is_github_repos
        self.has_start_command = has_start_command
        self.has_test_command = has_test_command

    def to_json(self):
        return {
            'project_name': self.project_name,
            'version': self.version,
            'description': self.description,
            'snap_store_name': self.snap_store_name,
            'icon_src': self.icon_src,
            'screenshot_src': self.screenshot_src,
            'author': self.author,
            'github_username': self.github_username,
            'author_linkedin_username': self.author_linkedin_username,
            'author_twitter_username': self.author_twitter_username,
            'author_website': self.author_website,
            'homepage': self.homepage,
            'project_demo_url': self.project_demo_url,
            'repository_url': self.repository_url,
            'contributing_url': self.contributing_url,
            'documentation_url': self.documentation_url,
            'license_url': self.license_url,
            'issues_url': self.issues_url,
            'license': self.license,
            'install_command': self.install_command,
            'usage_command': self.usage_command,
            'test_command': self.test_command,
            'repository': self.repository,
            'credits': self.credits,
            'is_github_repos': self.is_github_repos,
            'has_start_command': self.has_start_command,
            'has_test_command': self.has_test_command
        }

    @staticmethod
    def from_json(data: dict):
        return ReadmeModel(
            project_name=data.get("project_name", None),
            version=data.get("version", None),
            description=data.get("description", None),
            snap_store_name=data.get("snap_store_name", None),
            icon_src=data.get("icon_src", None),
            screenshot_src=data.get("screenshot_src", None),
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
