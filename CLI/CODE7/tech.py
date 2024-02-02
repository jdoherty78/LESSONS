import click

lang_list = ["Python", "JavaScript", "CSS", "C#"]

@click.group()
def cli():pass
@cli.group("consoles")
def my_consoles():pass

@my_consoles.command("fave")
def fave_console():
    click.secho("My favourite console is Xbox", fg="yellow")

@cli.group("computers")
def my_computers():pass

@my_computers.group()
def desktop():
    pass

@desktop.command("pc")
def pc_game():
    game = "Total War: Warhammer 3"
    click.secho("My favourite game is {}".format(game),
                fg = "red")

@my_computers.group()
def laptop():
    pass

@click.command()
@click.option("--lang", type = click.Choice(lang_list),
               default = "Python", 
               prompt = "What's your fave language?")
def language(lang):
    # lang = "Python"
    click.secho("My fave language is {}".format(lang),
               fg = "green")

laptop.add_command(language)

if __name__ == "__main__":
    cli()
    # cli("computers desktop pc".split(" "))
