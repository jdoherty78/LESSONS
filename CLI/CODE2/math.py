import click

@click.command()
@click.option("-n", nargs = 3, type = (int))

def sum_up(n):
    
    click.echo(n)

if __name__ == "__main__":
    sum_up()
