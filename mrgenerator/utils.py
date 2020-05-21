import json
import os.path


def create_json(lista):
    file = os.path.join(get_path_directory(), "readme.json")
    with open(file, 'w', encoding='utf-8') as outfile:
        json.dump(lista, outfile, indent=4, ensure_ascii=False, sort_keys=False)


def get_readme_json() -> dict:
    file = os.path.join(get_path_directory(), "readme.json")
    with open(file, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def get_templates_dir():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), "templates")


def get_path_directory():
    return os.getcwd()


def get_path_readme(path, name: str):
    return os.path.join(path, name)
