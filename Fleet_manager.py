def main():
    name, rank, division, ids = int_database()
    while True:
        display_menu()
        option = input("Select an option: ")
        if option == "1":
            add_member(name, rank, division, ids)
            print("Welcome to the fleet")
        elif option == "2":
            remove_member(name, rank, division, ids)
            print("Exiting the fleet, have a great day!")
            break
        elif option == "3":
            update_rank(name, rank, division, ids)
            print("Rank has been successfully updated.")