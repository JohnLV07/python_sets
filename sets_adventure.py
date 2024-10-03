# Task 1: Flight Route Comparison
'''
Objective: The aim of this assignment is to deepen your understanding and application of Python sets.

Imagine you work for an airline and need to compare the flight routes of your airline with a competitor.
You have two sets of flight destinations, one for each airline. Write a Python program to find out:

1. Destinations that both airlines fly to.

2. Destinations unique to your airline.

3. Whether there are any destinations that neither airline shares.

'''
# Basically find 3 Things:
    #-the similar destinations for both
    #- unique destionations for our
    # - Unique destinations for both


# Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

similar_destination = our_routes.intersection(competitor_routes)

unique_destinations = our_routes.symmetric_difference(competitor_routes)

our_unique = our_routes.difference(competitor_routes)



while True:
    print("\nFlight Route comparison")
    print("\n1: Similar destinations\n2: Our unique destinations\n3: Unique destination for both\n4: Exit ")
    choice = input("What do you want to see: ")
    if choice == '1':
        print(f" The routes that our competitors share with us are: {similar_destination}")
    elif choice == '2':
        print(f"Our unique Routes are: {our_unique}")
    elif choice == '3':
        print(f"The destinations that we don't share are: {unique_destinations}")
    elif choice == '4':
        print("Exiting the system.")
        break
    else:
        print("Invalid selection, try again.")

