def add_contact(name: str, phone: str, contacts):
    if name in contacts:
        return "This contact already exists"
    else:
        contacts[name] = phone
    return "Contact added"
