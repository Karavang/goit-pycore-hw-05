from modules.parse_input import parse_input
from modules.add_contant import add_contact
from modules.change_contact import change_contact
from modules.show_phone import show_phone
import os


def main():
    contacts = {}
    while True:
        command = input("Enter a command: ")
        parsed = parse_input(command)
        match parsed[0]:
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(parsed[1], parsed[2], contacts))
            case "change":
                print(change_contact(parsed[1], parsed[2], contacts))
            case "phone":
                print(show_phone(parsed[1], contacts))
            case "all":
                print(contacts)
            case "close" | "exit":
                try:
                    print("Good bye!")
                    # os.system('pkill -f "code"')
                    break
                except:
                    print("Failed to close the window")
            case _:
                print("Unknown command")


if __name__ == "__main__":
    main()
