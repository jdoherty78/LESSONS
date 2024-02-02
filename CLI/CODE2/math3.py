#python .\math3.py -n 10 -n 20 -n 100 -n 12 -n 99 -n 66
#(10, 20, 100, 12, 99, 66)
#Total 307
import click

@click.command()
@click.option("-n", multiple = True, type = (int))

def sum_up(n):
    
    click.echo(n)
    click.echo("Total {}".format(sum(n)))

if __name__ == "__main__":
    sum_up()
