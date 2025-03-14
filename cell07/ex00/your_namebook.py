def array_of_names(names_dict):
    # สร้างอาร์เรย์ของชื่อเต็มจาก dictionary ที่รับเข้ามา
    full_names = []
    for first_name, last_name in names_dict.items():
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        full_names.append(full_name)
    return full_names

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))