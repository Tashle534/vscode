import csv

with open("album.csv", mode= "rt") as file:
    reader= csv.reader(file)
    
    next(reader)
    
    for row in reader:
        album= row[0]
        artist = row[1]
        year = row[2]
        
        print ("Album Title : {album}")
        print("Artist : {artist}")
        print("Year : {year}")
        
import csv

with open("album.csv", mode= "rt") as file:
    reader= csv.DictReader(file)
    
    next(reader)
    
    for row in reader:
        print(f"Title: {row['album']}")
        print(f"Artist : {row['artist']}")
        print(f"Year : {row['year']}")
        