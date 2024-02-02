
#python .\auth3.py
#enter password: 
#confirm password:
#enter name: : boruto
#ERROR: Invalid name and/or password


#python .\auth3.py
#enter password: 
#confirm password:
#enter name: : naruto
#PASSWORD 123
#NAME: naruto



import click
users = [{"id": 1, "name": "naruto", "password": "123"},
         {"id": 2, "name": "hinata", "password": "444"},
         {"id": 3, "name": "sasuke", "password": "888"},]

name_list = [users[i]["name"] for i in range(len(users))]

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

    if name in name_list:
        click.echo("PASSWORD {}".format(password))
        click.echo("NAME: {}".format(name))
    else:
        click.echo("ERROR: Invalid name and/or password")

if __name__ == "__main__":
    login_user()
    



