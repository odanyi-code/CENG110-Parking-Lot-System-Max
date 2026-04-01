import unittest

from src.parking_lot import ParkingLot
from src.vehicle import Vehicle

import datetime

class TestParkingLot(unittest.TestCase):
    def setUp(self):
        """Set up a parking lot and some sample vehicles before each test."""
        self.lot = ParkingLot(capacity=2)
        self.v1 = Vehicle("ABC-123", "Alice", datetime.datetime.now())
        self.v2 = Vehicle("XYZ-789", "Bob", datetime.datetime.now())
        self.v3 = Vehicle("LMN-456", "Charlie", datetime.datetime.now())

    def test_parking_lot_creation(self):
        """Test creating an empty parking lot."""
        self.assertIsNotNone(self.lot)
        self.assertEqual(self.lot.check_availability(), 2)

    def test_vehicle_creation(self):
        """Test creating a vehicle."""
        self.assertIsNotNone(self.v1)
        self.assertEqual(self.v1.get_license_plate(), "ABC-123")

    def test_park_vehicle_success(self):
        """Verify a vehicle can be added to the lot."""
        success = self.lot.park_vehicle(self.v1)
        self.assertTrue(success)
        self.assertEqual(self.lot.check_availability(), 1)

    def test_park_vehicle_duplicate(self):
        """Verify adding a duplicate vehicle is rejected."""
        self.lot.park_vehicle(self.v1)
        # Attempt to park the same vehicle again
        success = self.lot.park_vehicle(self.v1)
        self.assertFalse(success)
        self.assertEqual(self.lot.check_availability(), 1)

    def test_park_vehicle_full(self):
        """Verify adding a vehicle to a full lot is rejected."""
        self.lot.park_vehicle(self.v1)
        self.lot.park_vehicle(self.v2)
        self.assertTrue(self.lot.is_full())

        # Lot is now full (capacity=2), attempt to park 3rd vehicle
        success = self.lot.park_vehicle(self.v3)
        self.assertFalse(success)
        self.assertEqual(self.lot.check_availability(), 0)

    def test_remove_vehicle_success(self):
        """Verify an existing vehicle can be removed."""
        self.lot.park_vehicle(self.v1)
        self.assertEqual(self.lot.check_availability(), 1)

        success = self.lot.remove_vehicle("ABC-123")
        self.assertTrue(success)
        self.assertEqual(self.lot.check_availability(), 2)

    def test_remove_vehicle_not_found(self):
        """Verify removing a non-existent vehicle is handled gracefully."""
        self.lot.park_vehicle(self.v1)
        success = self.lot.remove_vehicle("NON-EXISTENT")
        self.assertFalse(success)
        self.assertEqual(self.lot.check_availability(), 1)

    def test_check_availability(self):
        """Verify check_availability handles empty, partial, and full lots."""
        # Empty lot
        self.assertEqual(self.lot.check_availability(), 2)

        # Partially full
        self.lot.park_vehicle(self.v1)
        self.assertEqual(self.lot.check_availability(), 1)

        # Completely full
        self.lot.park_vehicle(self.v2)
        self.assertEqual(self.lot.check_availability(), 0)

if __name__ == '__main__':
    unittest.main()
