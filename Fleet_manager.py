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
            update_rank(name, rank , ids)
            print("Rank has been successfully updated.")
        elif option == "4":
            display_roster(name, rank, division, ids)
        elif option == "5":
            search_crew(name, rank, division, ids)
        elif option == "6":
            filter_by_division(name, division)
        elif option == "7":
            calculate_payroll(rank)
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
            print("8. Count officers by rank")
        def add_member(name, rank, division, ids):
            new_name = input("Enter the name of the new member: ")
            new_rank = input("Enter rank of new member: ")
            new_division = input("Enter division of new member: ")
            new_ids = (input("Enter ID of the new member: "))
            name_append = name.append(new_name)
            rank_append = rank.append(new_rank)
            division_append = division.append(new_division)
            ids_append = ids.append(new_ids)

        def remove_member(name, rank, division, ids):
            remove_name = input("Enter name of member to remove: ")
            remove_from_rank = rank.popindex(name.index(remove_name))
            remove_from_division = division.popindex(name.index(remove_name))
            remove_ids = ids.popindex(name.index(remove_name))

        def update_rank(name, rank, ids):
            update_name = input("Enter new name of member to update rank:")
            update_rank = input("Enter new rank of member:")
            update_ids  = int(input("Enter ID of member: "))
            name_index = name.index(update_name)
            rank(name_index) = update_rank
            ids(name_index) = update_ids
        
        def display_roster(name, rank, division, ids):
            print("name", "rank", "division", "ids")
            for i in range(len(name)): 
                print(name[i], rank[i], division[i], ids[i])

        def search_crew(name, rank, division, ids):
            search = input("Enter name of member to search: ")
            if search in name:
                index = name.index
                print("name:", name(index))
                print("rank:", rank(index))
                print("Division:", division(index))
                print("ID:", ids(index))
            else:
                print("Member not found. Please try again.")
        
        def filter_by_division(name, division):
            name = input("Enter name of member to filter by divisions: ")
            division = input("Enter division (command, operations, science, engineering, security):")
            print("name", "division")
            for i in range(len(name)):
                if division[i] == division:
                    print(name[i], division[i])

        def calculate_payroll(rank):
            
            
            
            
            ")


        



                




        

        



