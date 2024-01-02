import re

with open("contacts.csv", "r") as file:
    searchable = file.read()
    quary = input("Search for what: ")
    pattern = re.compile(rf".*{quary}.*")
    matches = pattern.findall(searchable)
    # matches = re.compile(rf".*{quary}.*").findall(searchable)
    #will take all the patter in our file 
    for match in matches:
        print(match)
