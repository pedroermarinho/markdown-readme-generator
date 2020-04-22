from generator import readme


class Generator(object):
    
    @staticmethod
    def run():
        readme.write_readme()
    
    def cli(self):
        pass
