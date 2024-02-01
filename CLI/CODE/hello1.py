import click

def hello(name, count):
    for i in range(count):
        click.echo("Hey {}".format(name))   #click.echo only likes 1 variable
        
if __name__ == "__main__":
    hello("Elita", 4)
