import os
from datetime import datetime

from jinja2 import Environment, FileSystemLoader
from mrgenerator import utils, infos


def write_readme(name=None, path=None):

    path = utils.get_path_directory() if path is None else path
    name = "README.md" if name is None else name

    env = Environment(loader=FileSystemLoader(utils.get_templates_dir()))
    template = env.get_template('default.pmd')
    filename = os.path.join(path, name)
    with open(filename, 'w') as fh:
        fh.write(template.render(
            data=infos.get_info_readme(),
            datetime=datetime
        ))
