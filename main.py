"""
Main Module
-----------
Entry point for the ParkingLotManagementSystem console application.
"""

import datetime
from src.parking_lot import ParkingLot
from src.vehicle import Vehicle

def main():
    """
    Main entry point for the application.
    """
    print("Welcome to the Parking Lot Management System!")

    # Initialize components here
    lot = ParkingLot(capacity=5)

    # Create some vehicles
    now = datetime.datetime.now()
    v1 = Vehicle("CAR-001", "Alice", now - datetime.timedelta(hours=2))
    v2 = Vehicle("CAR-002", "Bob", now)
    v3 = Vehicle("CAR-003", "Charlie", now - datetime.timedelta(hours=1))

    # Park vehicles in random order
    print("\n--- Parking Vehicles ---")
    lot.park_vehicle(v2)
    lot.park_vehicle(v1)
    lot.park_vehicle(v3)

    # Search for a vehicle
    print("\n--- Searching for Vehicle ---")
    search_plate = "CAR-003"
    print(f"Searching for {search_plate}...")
    found_vehicle = lot.search_vehicle(search_plate)
    if found_vehicle:
        print(f"Found: {found_vehicle}")

    print(f"Searching for NON-EXISTENT...")
    lot.search_vehicle("NON-EXISTENT")

    # Sort vehicles by entry time
    print("\n--- Sorting Vehicles by Entry Time ---")
    lot.sort_by_entry_time()

if __name__ == "__main__":
    main()
