import json
import os.path


def get_readme_json() -> dict:
    file = os.path.join(get_path_directory(), "readme.json")
    with open(file, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def get_template():
    return os.path.join("templates", "default.pmd")


def get_path_directory():
    return os.getcwd()


def get_path_readme():
    return os.path.join(get_path_directory(), "README.md")
