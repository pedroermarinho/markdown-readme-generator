class ReadmeModel:
    def __init__(self,
                 project_name: str,
                 version: str,
                 description: str,
                 author: str,
                 github_username: str,
                 author_website: str,
                 author_linkedin_username: str,
                 author_twitter_username: str,
                 homepage: str,
                 project_demo_url: str,
                 repository_url: str,
                 contributing_url: str,
                 documentation_url: str,
                 license_url: str,
                 issues_url: str,
                 license: str,
                 install_command: str,
                 usage_command: str,
                 test_command: str,
                 repository: dict,
                 credits: dict,
                 is_github_repos: bool,
                 has_start_command: bool,
                 has_test_command: bool
                 ):
        self.project_name = project_name
        self.version = version
        self.description = description
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
