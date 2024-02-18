import csv, os, sqlite3
FOLDER = "DATA"

### EXTRACT AUTHORS DATA
authors_list = []
with open(FOLDER + os.sep + "authors_info.csv", "r") as file:
    reading = csv.DictReader(file)
    for read in reading:
        authors_list.append(read)

### CREATE AUTHORS TABLE
conn = sqlite3.connect("bookstore.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Authors(
id INTEGER PRIMARY  KEY, 
author TEXT NOT NULL UNIQUE, -- Author name must be unique
published INTEGER NOT NULL, -- Number of Books published
nationality TEXT NOT NULL, -- Where the author was born
dob INTEGER NOT NULL -- Dat of birth
)
""")
### LOAD DATA
for author in authors_list:
    cursor.execute("""
    INSERT INTO Authors (author, published, nationality, dob)
    VALUES (?,?,?,?)
    """,(author["author"], int(author["published"]),
        author["nationality"], int(author["dob"])))
conn.commit()
conn.close()
print("Author's data inserted into the 'Authors' table.")
