#add decrypt function
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
    
    sub_folder = "enc_" + dt.now().strftime("%Y_%m_%d_%H_%M_%S")  # create  unique dir, starting with enc_for 
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

def list_all():
    folders = os.listdir(folder) # ENC
    for f in range(len(folders)):
        if folders[f].startswith("enc_"):
            print(f, folders[f])

    return folders

def decrypt_zip(zip_filename):
    folders = list_all()

    zf = input("Pick a zipfile to decrypt: ")
    
    folder_index_list = [str(folders.index(i)) for i in folders]
    if zf in folder_index_list:
        zf_int = int(zf)
        print(zf_int)
    else:
        print("Invalid input: Must be an integer")
        return

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
        
    with zipfile.ZipFile(full_path_zip, "r") as z:
        namelist = z.namelist()
        for file in namelist:
            z.extract(file)
            print(file)

    # rename decrypted folder
    enc_name = folder + os.sep + sub_folder
    dec_name = folder + os.sep + sub_folder.replace("enc", "dec")
    os.rename(enc_name, dec_name)
    os.system("start enc")

if __name__ == "__main__":   # make it Go!
    #encrypt_zip(zip_filename, files)   # run this!
    decrypt_zip(zip_filename)

