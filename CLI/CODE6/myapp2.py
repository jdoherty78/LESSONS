import click

@click.group()
def cli():pass

@cli.group()      #sub-group of @click, can create commands available in cli1, that are not available in  cli2
def cli1():pass

@cli1.command("init")
def init_app():
    click.echo("init app!")

@cli1.command("create")
def create_app():
    click.echo("create app!")


@cli.group()      #sub-group of @click
def cli2():pass

@cli2.command("info")
def author_info():
    name = "Cal Ripken Jr."
    click.echo("Author is {}".format(name))



if __name__ == "__main__":
    cli()


#python .\myapp2.py cli1
#Usage: myapp2.py cli1 [OPTIONS] COMMAND [ARGS]...
#
#Options:
#  --help  Show this message and exit.
#
#Commands:
#  create
#  init
#
# python .\myapp2.py cli1 init
# init app!
#
# python .\myapp2.py cli1 create
# create app!
#
#ython .\myapp2.py cli2
#Usage: myapp2.py cli2 [OPTIONS] COMMAND [ARGS]...
#
#Options:
#  --help  Show this message and exit.
#
#Commands:
#  info
#
# python .\myapp2.py cli2 info
# Author is Cal Ripken Jr.
#
#

