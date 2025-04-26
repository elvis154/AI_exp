def vacuum_cleaner_world():
    # User inputs for initial state
    dirt_left = input("Is there dirt on the left tile? (yes/no): ").strip().lower()
    dirt_right = input("Is there dirt on the right tile? (yes/no): ").strip().lower()

    # Initial state of the vacuum cleaner
    vacuum_position = input("Where is the vacuum cleaner initially? (left/right): ").strip().lower()

    # Initialize total cost
    total_cost = 0

    # Keep track of visited tiles
    visited_left = False
    visited_right = False

    while True:
        print(f"\nCurrent Position: {vacuum_position.capitalize()} Tile")

        if vacuum_position == "left":
            if dirt_left == "yes":
                print("Action: Suck dirt on the left tile.")
                dirt_left = "no"
                total_cost += 5
                print(f"Cost incurred: 5 | Total Cost: {total_cost}")
            visited_left = True
            print("Action: Move to the right tile.")
            vacuum_position = "right"

        elif vacuum_position == "right":
            if dirt_right == "yes":
                print("Action: Suck dirt on the right tile.")
                dirt_right = "no"
                total_cost += 5
                print(f"Cost incurred: 5 | Total Cost: {total_cost}")
            visited_right = True
            print("Action: Move to the left tile.")
            vacuum_position = "left"

        # Break the loop if both tiles are clean and both tiles have been visited
        if dirt_left == "no" and dirt_right == "no" and visited_left and visited_right:
            print("\nBoth tiles are clean.")
            print(f"Total cost of cleaning: {total_cost}")
            break

# Run the program
vacuum_cleaner_world()
