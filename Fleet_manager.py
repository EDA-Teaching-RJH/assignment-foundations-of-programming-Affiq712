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
            name = ["William Riker", "Deanna Troi", "Data", "Spock", "Paul chekov"]
            rank = ["Commander", "Lieutenant Commander", "Captain", "captain", "lieutenant"]
            division = ["Command", "Operations", "science", "Engineering", "Security"]
            ids = [1, 2, 3, 4, 5]
            return name, rank, division, ids
        def display_menu():
            print("Welcome to fleet management system")
            print("1. Add a crew member")
            print("2. Remove a crew member")
            print("3. update rank of crew member")
            print("4. Display roster")
            print("5. Search for crew member")
            print("6. Filter division")
            print("7. Calculate payroll")
        

        



