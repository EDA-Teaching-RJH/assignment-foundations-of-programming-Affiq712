def main():
    name, rank, division, ids = int_database()
    while True:
        choice = display_menu(name, rank, division, ids)
        if choice == "1":
    add_member(name, rank, division, ids)
elif choice == "2":
    remove_member(name, rank, division, ids)
    update_rank(name, rank, division, ids)
    display_roster(name, rank, division, ids)
    search_crew(name, rank, division, ids)