import zipfile, os, click    # zip files, access os, click to work with cli
from datetime import datetime as dt  # to create files named using date and time
from cryptography.fernet import Fernet  # fernet guarantees integrity of encrypted file, used for symmetric encryption
from werkzeug.security import (check_password_hash, generate_password_hash) 
# pip install cryptography zipfile
# create folder to contain encrypted files

folder = "ENC"  #folder to store encrypted files
zip_filename = "encrypted.zip"   #boiler plate filename
#files = os.listdir(".")  # list files in dir

@click.command()
@click.argument("command", type=click.Choice(["create", "decrypt"]))
@click.argument("files",nargs= -1, type=click.Path(exists=True))
@click.option("-pw", help="Enter a password to access zipfiles",
              hide_input = True, prompt = "Enter a password to access zipfiles")
                
def cli(command, files, pw):
    
    if not os.path.exists(folder):
        os.mkdir(folder) # ENC

    pw_path = folder + os.sep + "password.txt"

    if command == "create":

        pw_lower = pw.lower() # lower case
        pw_gen = generate_password_hash(pw_lower)

        if not os.path.exists(pw_path):
            ### CREATING PASSWORD FOR FIRST TIME
            with open(pw_path, "w") as w:
                w.write(pw_gen)

        else:   # replace existing password
            with open(pw_path, "w") as w:
                w.write(pw_gen)
        
        encrypt_zip(zip_filename, files)
        click.secho("Encrypted zipfile created successfully: {}".\
                    format(zip_filename), fg="red")

    elif command == "decrypt":

        with open(pw_path, "r") as r:
            pw_gen = r.readlines()[0]
            print("Check Password", pw_gen, pw)

            if check_password_hash(pw_gen, pw.lower()):
                # True or False
       
                decrypted_files = decrypt_zip(zip_filename)

                if decrypted_files is not None:
                    click.secho("""Zip folder decrypted successfully", fg="blue""")
                    click.secho("Decrypted files: ", fg="yellow")
                    for file in decrypted_files:
                        click.secho(file, fg="green")
            else:
                click.secho("Invalid password.", fg="green")

    else:
        click.secho("""Invalid input: \n 
                    Must be either create or decrypt""", fg="green")
        
                        
#print(files)     #list files in pwd

def encrypt_zip(zip_filename, files):    # begin function definition

    fernet_key = Fernet.generate_key() # key used to decrypt zipfiles
    cipher_suite = Fernet(fernet_key) # encrypt & decrypt
    
    sub_folder = "enc_" + dt.now().strftime("%Y_%m_%d_%H_%M_%S")  # create  unique dir, starting with enc_for 
    full_path = folder + os.sep + sub_folder # path to folder
    os.mkdir(full_path)   # make the folder
    #os.system("start .")  # same as cli, start in pwd
    
    with zipfile.ZipFile(full_path + os.sep + zip_filename, "w",
                         zipfile.ZIP_DEFLATED) as z:  # convert to zip file
        for file in files:    # iterate over files list
             z.write(file, os.path.basename(file))

    #store unique key, in unique dir
    with open(full_path + os.sep + "key.key", "wb") as key_file:
        key_file.write(fernet_key)
    #encrypt zip file
    with open(full_path + os.sep + zip_filename, "rb+") as z:
              encrypted_data = cipher_suite.encrypt(z.read())
              print("Encrypted Data")
              print(encrypted_data)
              z.seek(0)
              z.write(encrypted_data)

def list_all():
    folders = os.listdir(folder) # ENC
    for f in range(len(folders)):
        if folders[f].startswith("enc_"):
            print(f, folders[f])

    return folders

def decrypt_zip(zip_filename):
    folders = list_all()

    zf = input("Pick a zipfile to decrypt: ")
    
    folder_index_list = [str(folders.index(i)) for i in folders
                        if i.startswith("enc_")]
    if zf in folder_index_list:
        zf_int = int(zf)
        print(zf_int)
    else:
        print("Invalid input: Must be an integer")
        return None

    sub_folder = folders[zf_int]
    #print(sub_folder)

    full_path = folder + os.sep + sub_folder
    #creating fernet key from key.key
    with open(full_path + os.sep + "key.key", "rb") as key_file:
        fernet_key = key_file.read()
    cipher_suite = Fernet(fernet_key)

    # Decrypting zipfile
    full_path_zip = full_path + os.sep + zip_filename
    
    with open (full_path_zip, "rb") as z:
        decrypted_data = cipher_suite.decrypt(z.read())

    with open (full_path_zip, "wb") as z:
        z.write(decrypted_data)

    decrypted_files = []
    with zipfile.ZipFile(full_path_zip, "r") as z:
        namelist = z.namelist()
        for file in namelist:
            z.extract(file)
            print(file)
            decrypted_files.append(file)

    # rename decrypted folder
    enc_name = folder + os.sep + sub_folder
    dec_name = folder + os.sep + sub_folder.replace("enc", "dec")
    os.rename(enc_name, dec_name)
    #os.system("start enc")

    return decrypted_files

if __name__ == "__main__":   # make it Go!
    cli()
    #encrypt_zip(zip_filename, files)   # run this!
    #decrypt_zip(zip_filename)
    

