from generator import infos
import os.path

from generator.model.readme import ReadmeModel
from generator.readme import write_readme

if __name__ == '__main__':
    # version = 1
    # print('img alt ="Version" src ="https://img.shields.io/badge/version-{version}-blue.svg?cacheSeconds=2592000"/>'.format(version=version))
    write_readme()
    # a = infos.get_info_readme()
    # print(a.project_name)