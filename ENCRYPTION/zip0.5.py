import zipfile, os, click    # zip files, access os, click to work with cli
from datetime import datetime as dt  # to create files named using date and time

# pip install cryptography zipfile
# create folder to contain encrypted files

folder = "ENC"
zip_filename = "encrypted.zip"
files = os.listdir(".")

print(files)

