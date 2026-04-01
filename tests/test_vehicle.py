import unittest
import datetime
from src.vehicle import Vehicle

class TestVehicle(unittest.TestCase):
    def test_vehicle_initialization_and_getters(self):
        entry_time = datetime.datetime.now()
        vehicle = Vehicle(license_plate="ABC-123", owner_name="John Doe", entry_time=entry_time)

        self.assertEqual(vehicle.get_license_plate(), "ABC-123")
        self.assertEqual(vehicle.get_owner_name(), "John Doe")
        self.assertEqual(vehicle.get_entry_time(), entry_time)

    def test_vehicle_string_representation(self):
        entry_time = datetime.datetime(2023, 10, 27, 10, 30, 0)
        vehicle = Vehicle(license_plate="XYZ-987", owner_name="Jane Smith", entry_time=entry_time)

        expected_str = f"Vehicle(license_plate='XYZ-987', owner_name='Jane Smith', entry_time={entry_time})"
        self.assertEqual(str(vehicle), expected_str)
        self.assertEqual(repr(vehicle), expected_str)

if __name__ == '__main__':
    unittest.main()
