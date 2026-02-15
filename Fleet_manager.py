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
        elif option == "4":
            display_roster(name, rank, division, ids)
        elif option == "5":
            search_crew(name, rank, division, ids)
        elif option == "6":
            filter_by_division(name, division)
        elif option == "7":
            calculate_payroll(ranks)
        elif option == "8":
            count_officers(rank)
        else:
            print("Option not valid. Please try again. ")

        def int_database():
            name = ["William Riker", ""]

        



