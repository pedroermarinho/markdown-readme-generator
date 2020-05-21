from mrgenerator import readme
from mrgenerator.infos import create_info_json


class Generator(object):
    
    @staticmethod
    def start(name="README.md", path=None):
        readme.write_readme(name, path=path)

    @staticmethod
    def create():
        create_info_json()

