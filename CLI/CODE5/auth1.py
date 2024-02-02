#python.exe .\auth1.py
#enter password: 
#confirm password:
#Error: The two entered values do not match.
#enter password:
#confirm password:
#PASSWORD 123




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

def login_user(password):
    """This is a CLI authenticating citizens of the 
    hidden leaf village"""

    click.echo("PASSWORD {}".format(password))

if __name__ == "__main__":
    login_user()
    



