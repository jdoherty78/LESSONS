

#!/usr/bin/python
import click

color_list = ["blue", "red", "green", "yellow", "cyan", "white", "black"]

@click.command
@click.option("--color", default = "blue",
              type = click.Choice(color_list), prompt = "Enter a text color: ")



def colored(color):
    click.secho("Hello World!", fg = color)

if __name__ == '__main__':
    colored()




