# ParkingLotManagementSystem

## Project Description
ParkingLotManagementSystem is a console-based CENG110-level project designed to simulate the management of a small parking lot. The application demonstrates fundamental software engineering principles, specifically focusing on modular design, encapsulation, and the implementation of Abstract Data Types (ADTs) in Python. The system allows a user to park and remove vehicles, check the availability of parking spots, search for parked vehicles, and view all vehicles sorted by their entry time.

## Features Summary
- **Park a Vehicle**: Register a new vehicle with its license plate, owner's name, and automated entry time. Duplicate license plates are prevented.
- **Remove a Vehicle**: Unregister a vehicle from the parking lot using its license plate.
- **Check Availability**: View the number of available parking spots, along with clear notifications when the lot is completely empty or completely full.
- **Search for a Vehicle**: Retrieve details of a specific vehicle using its license plate.
- **Sort by Entry Time**: Reorder the parked vehicles chronologically based on when they entered the parking lot.

## Requirements & How to Run
### Requirements
- **Python**: Python 3.6 or higher is required.
- **Dependencies**: The application uses only Python's built-in libraries (`datetime`, `sys`). No external packages are needed.

### How to Run
1. Navigate to the root directory of the project.
2. Execute the application entry point using the following command:
   ```bash
   python main.py
   ```
3. Follow the on-screen console menu prompts to interact with the system.

## Testing Instructions
The system includes a suite of unit tests to verify the correctness of the ADTs and system features.

1. Ensure you are in the root directory of the project.
2. Run the test suite using Python's built-in `unittest` module:
   ```bash
   python -m unittest discover tests
   ```
3. The tests will output clear results to the console, confirming the success of core operations, edge cases, and invalid inputs.

## Directory Structure
- `src/`: Source code directory containing modules (`parking_lot.py`, `vehicle.py`, `simple_list.py`).
- `tests/`: Testing directory containing unit test cases.
- `report/`: Contains the final project report (`final_report.md`).
- `main.py`: The application entry point.
