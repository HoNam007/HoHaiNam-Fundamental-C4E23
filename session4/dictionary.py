person= {
    "doremon": "la meo may",
    "nobita": "la chu be hau dau",
    "shizuka": "la co be de thuong",
    "jaian": "la dua hay bat nobita",
    "suneo": "la dua hay khoe khoang",
}

while True:
    dic = input("Your code ?")
print(person[dic])
if dic in person:
    person[dic]
else:
    print("Not found")
    action = input("Contribute (Y/N)? ").upper()
    if action == "Y" or action == "YES",
        trans = input("Enter your tranlation:")
        person[dic] = trans






