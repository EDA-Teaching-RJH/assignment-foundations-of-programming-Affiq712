def main():
    name, rank, division, ids = int_database()
    while True:
        choice = display_menu()
    add_member(name, rank, division, ids)
    remove_member(name, rank, division, ids)
    update_rank(name, rank, division, ids)
    display_roster(name, rank, division, ids)
    search_crew(name, rank, division, ids)