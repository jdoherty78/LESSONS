import click

#@click.group()
#def cli():pass

@click.group(chain = False)      #sub-group of @click, can create commands available in cli1, that are not available in  cli2
def cli1():pass               # (chain = False) - is the default state

@cli1.command("init")
def init_app():
    click.echo("init app!")

@cli1.command("create")
def create_app():
    click.echo("create app!")


@click.group()      #sub-group of @click
def cli2():pass

@cli2.command("info")
def author_info():
    name = "Cal Ripken Jr."
    click.echo("Author is {}".format(name))

cli = click.CommandCollection(sources=[cli1, cli2])

if __name__ == "__main__":
    cli()

#python .\myapp5.py     <-- only have access to commands, no access to subgroups cli1 and cli2             
#Usage: myapp5.py [OPTIONS] COMMAND [ARGS]...
#
#Options:
#  --help  Show this message and exit.
#
#Commands:
#  create
#  info
#  init
