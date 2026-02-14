def main():
    name, rank, division, ids = int_database()
    while True:
        display_menu()
        option = input("Select an option: ")
        if option == "1":
            add_member(name, rank, division, ids)
        elif option == "2":
            remove_member(name, rank, division, ids)
        elif option == "3":
            update_rank(name, rank, division, ids)
        elif option == "4":
            display_roster(name, rank, division, ids)
        elif option == "5":
            search_member(name, rank, division, ids)
        elif option == "6":
            filter_by_division(name, rank, division, ids)
        elif option == "7":
            calculate_payroll(name, rank, division, ids)
        elif option == "8":
            count_officers(name, rank, division, ids)
        elif option == "9":
            print("Exiting the program. Have a great day!")
            break
        else:
            print("Invalid option. Please try again.")

        def int_database():
            name = ()
        

        def display_menu():
            print("\n--- Fleet Management System ---")
            print("1. Add Member")
            print("2. Remove Member")
            print("3. Update Rank")
            print("4. Display Roster")
            print("5. Search Member")
            print("6. Filter by Division")
            print("7. Calculate Payroll")
            print("8. Count Officers")
            print("9. Exit")

        def int_database():
            name = ("William Riker", "Pavel Chekov", "Deanna Troi", "Data", "Beverly Crusher")
            rank = ("Commander", "Captain", "Lieutenant Commander", "Lieutenant Commander", "Commander")
            division = ("Operations", "Science", "Command", "Engineering", "Medical")
            ids = [1001, 1002, 1003, 1004, 1005]
            return name, rank, division, ids