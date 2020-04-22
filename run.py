from generator import get_info_readme
from generator.generator import Generator
from generator.model.readme import ReadmeModel

if __name__ == '__main__':
    app = Generator()
    app.run()

    # var = get_info_readme()
    # print(var.credits.__len__())
    # for i in var.credits:
    #     print(var.credits[i]["type"])
    #     print(var.credits[i]["name"])
    #     print(var.credits[i]["url"])
