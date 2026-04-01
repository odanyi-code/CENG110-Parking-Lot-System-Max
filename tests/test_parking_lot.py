import unittest

from src.parking_lot import ParkingLot
from src.vehicle import Vehicle

class TestParkingLot(unittest.TestCase):
    def test_parking_lot_creation(self):
        """Test creating an empty parking lot."""
        lot = ParkingLot()
        self.assertIsNotNone(lot)

    def test_vehicle_creation(self):
        """Test creating a vehicle."""
        vehicle = Vehicle()
        self.assertIsNotNone(vehicle)

if __name__ == '__main__':
    unittest.main()
