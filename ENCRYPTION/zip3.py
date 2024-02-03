
import zipfile, os, click    # zip files, access os, click to work with cli
from datetime import datetime as dt  # to create files named using date and time
from cryptography.fernet import Fernet  # fernet guarantees integrity of encrypted file, used for symmetric encryption

# pip install cryptography zipfile
# create folder to contain encrypted files

folder = "ENC"  #folder to store encrypted files
zip_filename = "encrypted.zip"   #boiler plate filename
files = os.listdir(".")  # list files in dir

#print(files)     #list files in pwd

def encrypt_zip(zip_filename, files):    # begin function definition

    fernet_key = Fernet.generate_key() # key used to decrypt zipfiles
    cipher_suite = Fernet(fernet_key) # encrypt & decrypt
    
    sub_folder = dt.now().strftime("%Y_%m_%d_%H_%M_%S")  # create unique dir everytime the function is run
    full_path = folder + os.sep + sub_folder # path to folder
    os.mkdir(full_path)   # make the folder
    os.system("start .")  # same as cli, start in pwd
    
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

if __name__ == "__main__":   # make it Go!
    encrypt_zip(zip_filename, files)   # run this!

