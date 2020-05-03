<h1 align="center">
{%if data.icon_src is not none %}<img src="{{data.icon_src}}" height="200" width="200"><br/>{% endif %}
{%if data.project_name is not none %}Welcome to {{data.project_name}} 👋{% endif %}
{%if data.snap_store_name is not none %}<a href="https://snapcraft.io/{{data.snap_store_name}}"> <br/> <img src="https://github.com/snapcore/snap-store-badges/raw/master/PT/%5BPT%5D-snap-store-black-uneditable%401x.png"></a>{% endif %}
</h1>
<p>
{% if data.version is not none %}<img alt="Version" src="https://img.shields.io/badge/version-{{data.version}}-blue.svg?cacheSeconds=2592000" />{% endif %}
{% if data.documentation_url is not none %}<a href="{{data.documentation_url}}" target="_blank"><img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" /></a>{% endif %}
{%if data.is_github_repos is not none and data.is_github_repos==True %}<a href="{{data.repository_url}}/graphs/commit-activity" target="_blank"><img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" /></a>{% endif %}
{%if data.license is not none %}<a href="{{data.license_url}}" target="_blank"><img alt="License:{{data.license}}" src="https://img.shields.io/badge/License-{{data.license}}-yellow.svg" /></a>{% endif %}
{%if data.author_twitter_username is not none %}<a href="https://twitter.com/{{data.author_twitter_username}}" target="_blank"><img alt="Twitter: {{data.author_twitter_username}}" src="https://img.shields.io/twitter/follow/{{data.author_twitter_username}}.svg?style=social" /></a>{% endif %}
</p>

{%if data.description is not none %}> {{data.description}}{% endif %}
{%if data.homepage is not none %}### 🏠 [Homepage]({{data.homepage}}){% endif %}
{%if data.project_demo_url is not none %}### ✨ [Demo]({{data.project_demo_url}}){% endif %}
{%if data.install_command is not none and data.install_command.__len__()>0%}## Install
```sh
{%for install_command in data.install_command %}{{install_command}}
{% endfor %}
```
{% endif %}
{%if data.usage_command is not none and data.usage_command.__len__()>0 %}## Usage
```sh
{%for usage_command in data.usage_command %}{{usage_command}}
{% endfor %}
```
{% endif %}
{%if data.test_command is not none  and data.test_command.__len__()>0%}## Run tests
```sh
{%for test_command in data.test_command %}{{test_command}}
{% endfor %}
```
{% endif %}
{%if data.author is not none or data.author_twitter_username is not none or data.github_username is not none %}## Author
{%if data.author is not none %}👤 **{{data.author}}**{% endif %}
{%if data.author_website is not none %}* Website: {{data.author_website}}{% endif %}
{%if data.author_twitter_username is not none %}* Twitter: [@{{data.author_twitter_username}}](https://twitter.com/{{data.author_twitter_username}}){% endif %}
{%if data.github_username is not none %}* GitHub: [@{{data.github_username}}](https://github.com/{github_username}){% endif %}
{%if data.author_linkedin_username is not none %}* LinkedIn: [@{{data.author_linkedin_username}}](https://linkedin.com/in/{author_linkedin_username}){% endif %}
{% endif %}
{%if data.screenshot_src is not none and data.screenshot_src.__len__()>0 %}## 📸 Screenshot
<h1 align="center">
{%for screenshot_src in data.screenshot_src %}
<img src="{{screenshot_src}}" alt="{{data.project_name}}">
{% endfor %}
</h1>{% endif %}

{%if data.issues_url is not none %}## 🤝 Contributing
Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page]({{data.issues_url}}). You can also take a look at the [contributing guide]({{data.contributing_url}}){% endif %}
## Show your support
Give a ⭐️ if this project helped you!
{%if data.credits is not none and data.credits.__len__()>0 %}## Credits{%for credits in data.credits %}
**[{{credits["name"]}}]({{credits["url"]}})**{% endfor %}{% endif %}
{%if data.license is not none and data.license_url is not none %}## 📝 License
{%if data.author is not none and data.github_username is not none %}
Copyright © {{datetime.today().year}} [{{data.author}}](https://github.com/{{data.github_username}} ).<br/>{% endif %}
This project is [{{data.license}}]({{data.license_url}}) licensed.{% endif %}

---
_This README was created with the [markdown-readme-generator](https://github.com/pedroermarinho/markdown-readme-generator)_