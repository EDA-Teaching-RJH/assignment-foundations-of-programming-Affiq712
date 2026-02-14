def main():
    name, rank, division , ids = int_databse()
    while True:
        display_menu()
        option = input("Select an option: ")
        if option == "1":
            add_member(name, rank, divsion, ids)
        elif option == "2":
            remove_member(name, rank, division, ids)
        elif option == "3":
            update_rank(name, rank, division, ids)
        elif option == "4":
            display_roster(name, rank, division, ids)
        elif option == "5":
            search_member(name, rank, division, ids)
        elif option == "6":
            filter_by division(name, rank, division, ids)