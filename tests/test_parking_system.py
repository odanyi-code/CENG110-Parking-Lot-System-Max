import unittest
import datetime
from src.parking_lot import ParkingLot
from src.vehicle import Vehicle

class TestParkingSystem(unittest.TestCase):
    def setUp(self):
        """Set up an empty parking lot for testing."""
        self.lot = ParkingLot(capacity=3)
        self.v1 = Vehicle("PLATE-1", "Alice", datetime.datetime.now())
        self.v2 = Vehicle("PLATE-2", "Bob", datetime.datetime.now())
        self.v3 = Vehicle("PLATE-3", "Charlie", datetime.datetime.now())

    def test_01_park_normal_case(self):
        """Normal case: Park 3 vehicles successfully."""
        print("\nRunning Test: Normal case (Park 3 vehicles successfully)")
        self.assertTrue(self.lot.park_vehicle(self.v1))
        self.assertTrue(self.lot.park_vehicle(self.v2))
        self.assertTrue(self.lot.park_vehicle(self.v3))
        self.assertEqual(self.lot.check_availability(), 0)

    def test_02_edge_case_empty(self):
        """Edge case (empty): Remove or search when lot is empty."""
        print("\nRunning Test: Edge case (Remove/search when lot is empty)")
        self.assertFalse(self.lot.remove_vehicle("NON-EXISTENT"))
        self.assertIsNone(self.lot.search_vehicle("NON-EXISTENT"))

    def test_03_invalid_input(self):
        """Invalid input: Try to park a non-Vehicle type (handle gracefully)."""
        print("\nRunning Test: Invalid input (Try to park a non-Vehicle type)")
        invalid_vehicle = "This is not a vehicle"
        self.assertFalse(self.lot.park_vehicle(invalid_vehicle))

    def test_04_duplicate_record(self):
        """Duplicate record: Try parking a car with the same license plate twice."""
        print("\nRunning Test: Duplicate record (Try parking a car with the same license plate twice)")
        self.lot.park_vehicle(self.v1)
        self.assertFalse(self.lot.park_vehicle(self.v1))

    def test_05_full_lot(self):
        """Full lot: Try to park a vehicle when the lot is full."""
        print("\nRunning Test: Full lot (Try to park a vehicle when the lot is full)")
        self.lot.park_vehicle(self.v1)
        self.lot.park_vehicle(self.v2)
        self.lot.park_vehicle(self.v3)
        # Lot is now full (capacity 3)
        v4 = Vehicle("PLATE-4", "Dave", datetime.datetime.now())
        self.assertFalse(self.lot.park_vehicle(v4))

if __name__ == '__main__':
    unittest.main(verbosity=2)
