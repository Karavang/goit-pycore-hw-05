def show_phone(name, contacts):
    if name in contacts:
        return contacts[name]
    else:
        return "Unknown name"
