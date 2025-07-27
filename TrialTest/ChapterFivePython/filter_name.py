def get_last_name(names_of_people):
    return list(filter(lambda name: name[1].lower() == "jones", names_of_people))
list_of_names = [
    ("jayson", "jones"),
    ("Bob ","Carol"),
    ("David", "jones"),
    ("john", "vincent"),
    ("Motunrayo", "jones")
]

result = get_last_name(list_of_names)

print(result)
