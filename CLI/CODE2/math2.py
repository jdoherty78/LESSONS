#math2.py -n 10 -n 20 -n 99
import click

@click.command()
@click.option("-n", multiple = True, type = (int))

def sum_up(n):
    
    click.echo(n)

if __name__ == "__main__":
    sum_up()
