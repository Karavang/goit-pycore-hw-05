def change_contact(name: str, phone: str, contacts):
    if name in contacts:
        contacts[name] = phone
    return "Contact changed"
