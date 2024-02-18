import csv, os, sqlite3
FOLDER = "DATA"
data_curr = [] ### CURRENT_AUTHORS_BOOKS.csv
data_legacy = [] ### LEGACY_AUTHORS_BOOKS.csv

### EXTRACT DATA
### LEGACY AUTHORS
with open(FOLDER + os.sep +\
          "legacy_authors_books.csv", "r") as file:
    reading = csv.DictReader(file)
    for row in reading:
        data_legacy.append({
            "author_id": row["id"],
            "author": row["Author Name"],
            "title": row["Book Title"],
            "price": float(row["Price (GBP)"]),
        })
### CURRENT AUTHORS
with open(FOLDER + os.sep +\
          "current_authors_books.csv", "r") as file:
    reading = csv.DictReader(file)
    for row in reading:
        data_curr.append({
            "author_id": row["id"],
            "author": row["Author Name"],
            "title": row["Book Title"],
            "price": float(row["Price (GBP)"]),
        })
print(len(data_legacy))
