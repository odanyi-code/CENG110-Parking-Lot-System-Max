"""
ParkingLot Module
-----------------
This module defines the ParkingLot Abstract Data Type (ADT).
"""

from src.simple_list import SimpleList
from src.vehicle import Vehicle

class ParkingLot:
    """
    Represents a parking lot management system.

    This class encapsulates the management of parking spaces and vehicles.
    """
    def __init__(self, capacity: int = 10):
        """
        Initializes a new ParkingLot instance.
        """
        self._capacity = capacity
        self._vehicles = SimpleList()

    def is_full(self) -> bool:
        """Checks if the parking lot is full."""
        return self._vehicles.size() >= self._capacity

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        """
        Parks a vehicle if the lot is not full and it's not a duplicate.
        """
        if not isinstance(vehicle, Vehicle):
            print("Invalid input: Only Vehicle instances can be parked.")
            return False

        if self.is_full():
            print(f"Parking lot is full. Cannot park vehicle {vehicle.get_license_plate()}.")
            return False

        for v in self._vehicles.get_all():
            if v.get_license_plate() == vehicle.get_license_plate():
                print(f"Vehicle with license plate {vehicle.get_license_plate()} is already parked.")
                return False

        self._vehicles.add(vehicle)
        print(f"Vehicle {vehicle.get_license_plate()} parked successfully.")
        return True

    def remove_vehicle(self, license_plate: str) -> bool:
        """
        Removes a vehicle by license plate if it exists.
        """
        for v in self._vehicles.get_all():
            if v.get_license_plate() == license_plate:
                self._vehicles.remove(v)
                print(f"Vehicle {license_plate} removed successfully.")
                return True

        print(f"Vehicle {license_plate} not found in the parking lot.")
        return False

    def search_vehicle(self, license_plate: str) -> Vehicle | None:
        """
        Search for a vehicle by license plate.
        """
        for v in self._vehicles.get_all():
            if v.get_license_plate() == license_plate:
                return v

        print("Vehicle not found.")
        return None

    def sort_by_entry_time(self):
        """
        Sorts the parked vehicles by their entry time.
        """
        vehicles = self._vehicles.get_all()

        vehicles.sort(key=lambda v: v.get_entry_time())

        # Rebuild the internal list
        self._vehicles = SimpleList()
        for v in vehicles:
            self._vehicles.add(v)

    def get_parked_vehicles(self):
        """
        Returns a shallow copy of the list of parked vehicles.
        """
        return self._vehicles.get_all()

    def check_availability(self) -> int:
        """
        Returns the number of free spots and prints status messages.
        """
        free_spots = self._capacity - self._vehicles.size()

        if self._vehicles.is_empty():
            print("The parking lot is completely empty.")
        elif self.is_full():
            print("The parking lot is completely full.")
        else:
            print(f"There are {free_spots} free spots available.")

        return free_spots
