"""
Vehicle Module
--------------
This module defines the Vehicle Abstract Data Type (ADT).
"""

import datetime

class Vehicle:
    """
    Represents a vehicle in the parking lot.

    This class encapsulates the properties and behaviors associated with a generic vehicle.
    As an Abstract Data Type (ADT), it hides its internal state using private attributes
    and exposes functionality through well-defined public methods (getters). This adheres
    to the principle of encapsulation.
    """
    def __init__(self, license_plate: str, owner_name: str, entry_time: datetime.datetime):
        """
        Initializes a new Vehicle instance.

        Args:
            license_plate (str): The license plate of the vehicle.
            owner_name (str): The name of the vehicle's owner.
            entry_time (datetime.datetime): The time the vehicle entered the parking lot.
        """
        self.__license_plate = license_plate
        self.__owner_name = owner_name
        self.__entry_time = entry_time

    def get_license_plate(self) -> str:
        """
        Gets the vehicle's license plate.
        """
        return self.__license_plate

    def get_owner_name(self) -> str:
        """
        Gets the name of the vehicle's owner.
        """
        return self.__owner_name

    def get_entry_time(self) -> datetime.datetime:
        """
        Gets the time the vehicle entered the parking lot.
        """
        return self.__entry_time

    def __str__(self) -> str:
        """
        Returns a formatted string representation of the Vehicle.
        """
        return f"Vehicle(license_plate='{self.__license_plate}', owner_name='{self.__owner_name}', entry_time={self.__entry_time})"

    def __repr__(self) -> str:
        """
        Returns a formal string representation of the Vehicle.
        """
        return self.__str__()
