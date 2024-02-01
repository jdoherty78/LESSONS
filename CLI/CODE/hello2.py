import click

@click.command()
@click.option("--name")
@click.option("--count", default = 1)

def hello(name, count):
    for i in range(count):
        click.echo("Hey {}".format(name))   #click.echo only likes 1 variable
        
if __name__ == "__main__":
    hello()


    

#python .\hello2.py --name Joe
#Hey Joe
# python .\hello2.py --name Joe --count 3 
#Hey Joe
#Hey Joe
#Hey Joe
#
