import pweave

from generator import utils


def write_readme():
    file = utils.get_template()

    pweave.weave(file, doctype="markdown", plot=False, output=utils.get_path_readme())
