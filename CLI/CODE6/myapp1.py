import click

@click.group()
def cli():pass

@cli.group()      #sub-group of @click, can create commands available in cli1, that are not available in  cli2
def cli1():pass

@cli1.command()
def init_app():
    click.echo("init app!")

@cli1.command()
def create_app():
    click.echo("create app!")


@cli.group()      #sub-group of @click
def cli2():pass

@cli2.command()
def author_info():
    name = "Cal Ripken Jr."
    click.echo("Author is {}".format(name))



if __name__ == "__main__":
    cli()


#python .\myapp1.py cli1
#Usage: myapp1.py cli1 [OPTIONS] COMMAND [ARGS]...
#
#Options:
#  --help  Show this message and exit.
#
#Commands:
#  create-app
#  init-app

#python .\myapp1.py cli1 init-app
#init app!


#python .\myapp1.py          Usage: myapp1.py [OPTIONS] COMMAND [ARGS]...
#Options:
#  --help  Show this message and exit.
#
#Commands:
#  cli1
#  cli2

# python .\myapp1.py cli1 create-app
# create app!

#python .\myapp1.py cli2
#Usage: myapp1.py cli2 [OPTIONS] COMMAND [ARGS]...
#
#Options:
#  --help  Show this message and exit.
#
#Commands:
#  author-info

# python .\myapp1.py cli2 author-info
# Author is Cal Ripken Jr.


