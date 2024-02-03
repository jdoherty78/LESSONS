
import zipfile, os, click    # zip files, access os, click to work with cli
from datetime import datetime as dt  # to create files named using date and time

# pip install cryptography zipfile
# create folder to contain encrypted files

folder = "ENC"  #folder to store encrypted files
zip_filename = "encrypted.zip"   #boiler plate filename
files = os.listdir(".")  # list files in dir

#print(files)     #list files in pwd

def encrypt_zip(zip_filename, files):    # begin function definition
    sub_folder = dt.now().strftime("%Y_%m_%d_%H_%M_%S")  # create dir based on time the function runs
    full_path = folder + os.sep + sub_folder # path to folder
    os.mkdir(full_path)   # make the folder
    os.system("start .")  # same as cli, start in pwd
    with zipfile.ZipFile(full_path + os.sep + zip_filename, "w",
                         zipfile.ZIP_DEFLATED) as z:  #convert to zip file
        for file in files:    # iterate over files list
            # file = "C:/Users/joedo/Documents/info.txt"
            # os.path.dirname(file)
            # OUTPUT
            # C:/Users/joedo/Documents/ #HEAD
            # os.path.basename(file)
            # OUTPUT
            # info.txt # TAIL
            z.write(file, os.path.basename(file))

if __name__ == "__main__":   # make it Go!
    encrypt_zip(zip_filename, files)   # run this!

