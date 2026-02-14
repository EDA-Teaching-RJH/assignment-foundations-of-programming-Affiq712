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

        
        

        def display_menu():
            print(" Welcome to the Fleet Managment System")
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
        
        def add_member(name, rank, division, ids):
            new_name = input("Enter the name of new member: ")
            new_rank = input("Enter the rank of new member: ")
            new_division = input("Enter the division of the new member: ")
            new_id = int(input("Enter the ID of the new member: "))
            name.append(new_name)
            rank.append(new_rank)
            division.append(new_division)
            ids.append(new_id)
            print(f"{new_name} has been added to the fleet ")
            
        
            