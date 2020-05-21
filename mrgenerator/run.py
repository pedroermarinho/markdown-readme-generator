import click

from mrgenerator.generator import Generator

app = Generator()


@click.group()
def cli():
    """
    Markdown Readme Generator

    Gerador de readme.
    """
    pass


@cli.command('start')
@click.option('--name', '--n', type=str, default='README.md', help="Nome do arquivo a ser gerado")
@click.option('--path', '--p', type=str, default=None, help="Caminho do arquivo a ser gerado")
def start(name, path):
    """
    build readme.md.

    construir readme.md.
    """
    app.start(name, path)


@cli.command('create')
def create():
    """
    create build file readme.json.

    criar arquivo de construção readme.json.
    """
    app.create()


if __name__ == '__main__':
    cli()
