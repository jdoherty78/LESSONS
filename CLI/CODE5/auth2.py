#python.exe .\auth2.py
#enter password: 
#confirm password:
#enter name: : joe
#PASSWORD 123
#NAME: joe



import click
users = [{"id": 1, "name": "naruto", "password": "123"},
         {"id": 2, "name": "hinata", "password": "444"},
         {"id": 3, "name": "sasuke", "password": "888"},]

@click.command()
@click.option("--password", type = str, 
              prompt = "enter password", 
              hide_input = True,
              confirmation_prompt = "confirm password", 
              help = "enter password and confirm password")

@click.option("--name", type = str, 
              prompt = "enter name: ",
              help = "enter name from hidden village",
              required = True)

def login_user(name, password):
    """This is a CLI authenticating citizens of the 
    hidden leaf village"""

    click.echo("PASSWORD {}".format(password))
    click.echo("NAME: {}".format(name))

if __name__ == "__main__":
    login_user()
    



