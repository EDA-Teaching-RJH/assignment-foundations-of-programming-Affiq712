def main():
    name, rank, division, ids = int_database()
    while True:
        choice = display_menu(name, rank, division, ids)
        if choice == "1":
    add_member(name, rank, division, ids)
elif choice == "2":
    remove_member(name, rank, division, ids)
    print("Member has been removed.")
    break
elif choice == "3":
    update_rank(name, rank, division, ids)
    print("Rank updated.")
elif choice == "4":
    display_roster(name, rank, division, ids)
elif choice == "5":
    search_crew(name, rank, division, ids)
elif choice == "6":
    filter_by_division(name, rank, division, ids)
elif choice =="7":
    calculate_payroll()
elif choice =="8":
    count_officers(name, rank, division, ids)
else: 
    print("Invalid option. Please try again.")

