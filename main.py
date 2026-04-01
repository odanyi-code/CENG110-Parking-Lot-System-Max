"""
Main Module
-----------
Entry point for the ParkingLotManagementSystem console application.
"""

import datetime
import sys
from src.parking_lot import ParkingLot
from src.vehicle import Vehicle

def display_menu():
    """Displays the main menu options."""
    print("\n--- Parking Lot Management System ---")
    print("1. Park a vehicle")
    print("2. Remove a vehicle")
    print("3. Check availability")
    print("4. Search vehicle")
    print("5. Sort by entry time")
    print("6. Exit")
    print("-------------------------------------")

def main():
    """
    Main entry point for the application.
    """
    print("Welcome to the Parking Lot Management System!")

    # Initialize parking lot with a default capacity
    lot = ParkingLot(capacity=10)

    while True:
        display_menu()
        choice_str = input("Enter your choice (1-6): ").strip()

        if not choice_str:
            print("Please enter a valid choice.")
            continue

        try:
            choice = int(choice_str)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            plate = input("Enter license plate: ").strip()
            if not plate:
                print("License plate cannot be empty.")
                continue

            owner = input("Enter owner name: ").strip()
            if not owner:
                print("Owner name cannot be empty.")
                continue

            entry_time = datetime.datetime.now()
            vehicle = Vehicle(plate, owner, entry_time)
            lot.park_vehicle(vehicle)

        elif choice == 2:
            plate = input("Enter license plate to remove: ").strip()
            if not plate:
                print("License plate cannot be empty.")
                continue

            lot.remove_vehicle(plate)

        elif choice == 3:
            lot.check_availability()

        elif choice == 4:
            plate = input("Enter license plate to search: ").strip()
            if not plate:
                print("License plate cannot be empty.")
                continue

            found_vehicle = lot.search_vehicle(plate)
            if found_vehicle:
                print(f"Vehicle found: {found_vehicle}")

        elif choice == 5:
            lot.sort_by_entry_time()
            print("Vehicles have been sorted by entry time.")

        elif choice == 6:
            print("Exiting the Parking Lot Management System. Goodbye!")
            sys.exit(0)

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
