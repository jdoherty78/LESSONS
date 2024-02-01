import click

@click.command()
@click.option("--name", prompt = True, help = "Enter a name to greet")
@click.option("--count", default = 1)

def hello(name, count):
    """This is a docstring for this python function"""
    for i in range(count):
        click.echo("Hey {}".format(name))   #click.echo only likes 1 variable
        
if __name__ == "__main__":
    hello()


#python .\hello3.py                     
#Name: Hanna
#Hey Hanna

#python .\hello3.py --count 3     
#Name: Baruto
#Hey Baruto
#Hey Baruto
#Hey Baruto


#python .\hello3.py --help   
#Usage: hello3.py [OPTIONS]

#Options:
#  --name TEXT      Enter a name to greet
#  --count INTEGER
#  --help           Show this message and exit.
#PS C:\Users\joedo\Desktop\LESSONS\CLI\CODE> 

#python .\hello3.py       
#Name: Himawari
#Hey Himawari

#python .\hello3.py --help
#Usage: hello3.py [OPTIONS]
#
#  This is a docstring for this python function
#
#Options:
#  --name TEXT      Enter a name to greet
#  --count INTEGER
#  --help           Show this message and exit.


