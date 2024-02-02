import click

#python .\pet.py
#meow
#snooring


#python .\pet.py woof 4
#woof
#woof
#woof
#woof
#snooring



#python .\pet.py woof 4 --sleep False
#woof
#woof
#woof
#woof

# python .\pet.py woof 4 --help       
#Usage: pet.py [OPTIONS] [SOUND] [N]

#  This is a dcostring for the noisey pet function

#Options:
#  --sleep BOOLEAN  Does your pet snore?
#  --help           Show this message and exit.

@click.command()
@click.argument("sound", type = str, default = "meow")
@click.argument("n", type = int, default = 1)
@click.option("--sleep", default = True, help = "Does your pet snore?")
def noisey_pet(sound, n, sleep):
    """This is a dcostring for the noisey pet function"""
    for _ in range(n):
        click.echo(sound)

    if sleep:
        click.echo("snooring")

if __name__ == "__main__":
    noisey_pet()
