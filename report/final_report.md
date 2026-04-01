# Parking Lot Management System Final Report

## 1. Project Overview
The Parking Lot Management System is a CENG110-level console application implemented in Python. It simulates the basic operations of managing a small parking lot, focusing on the application of fundamental software engineering principles. The project emphasizes modular design, Abstract Data Types (ADTs), and the principle of encapsulation.

## 2. ADT Design and Encapsulation
The project's architecture revolves around defining and implementing robust ADTs to represent the core entities in the system.

*   **Vehicle ADT (`src/vehicle.py`)**
    *   The `Vehicle` class encapsulates the state of an individual vehicle, including its `license_plate`, `owner_name`, and `entry_time`.
    *   **Encapsulation:** The internal state is strictly protected using double underscores (e.g., `__license_plate`), preventing direct access or modification from outside the class.
    *   Access to these attributes is carefully controlled through public getter methods (e.g., `get_license_plate()`), ensuring the data remains consistent and cannot be inadvertently altered after the vehicle is created.
*   **ParkingLot ADT (`src/parking_lot.py`)**
    *   The `ParkingLot` class models the entire parking facility. It maintains the overall `_capacity` and a collection of parked `_vehicles`.
    *   **Encapsulation:** The underlying collection of vehicles is hidden within the `ParkingLot` class. Operations such as parking, removing, or searching for a vehicle are exposed as well-defined public methods (`park_vehicle`, `remove_vehicle`, `search_vehicle`).
    *   This strict encapsulation ensures that client code (like `main.py`) cannot manipulate the raw list of vehicles directly. Client code must interact with the parking lot through its defined interface, allowing the `ParkingLot` class to enforce business rules (e.g., checking for capacity limits or duplicate license plates).

## 3. Data Structure Choice and Justification
The system requires a data structure to maintain the collection of parked vehicles.

*   **Custom SimpleList Wrapper (`src/simple_list.py`)**
    *   **Choice:** The collection of vehicles is managed using a custom `SimpleList` class, which wraps a built-in Python `list`.
    *   **Justification:** While a standard Python list is used internally, the `SimpleList` wrapper is critical for maintaining the integrity of the `ParkingLot` ADT. By hiding the standard list operations, the `SimpleList` ensures that operations like dynamic resizing, indexing, and removal are handled predictably.
    *   The standard Python list offers excellent performance characteristics for typical operations: O(1) appending and O(N) indexing/removal.
    *   The wrapper prevents arbitrary modifications to the underlying list from external sources, strictly enforcing the encapsulation principle.

## 4. Functional Overview
The system provides a clear, beginner-friendly console interface with the following primary functionalities:

*   **Park a Vehicle (`park_vehicle`):** Users can input a vehicle's license plate and owner name. The system captures the current time as the entry time. The system prevents parking if the lot is full or if the license plate is already registered.
*   **Remove a Vehicle (`remove_vehicle`):** Vehicles can be removed by providing their license plate. The system confirms removal or notifies the user if the vehicle is not found.
*   **Check Availability (`check_availability`):** Displays the number of remaining free spots. It provides explicit feedback when the lot is completely empty or completely full.
*   **Search for a Vehicle (`search_vehicle`):** Allows users to look up a parked vehicle by its license plate and displays its details.
*   **Sort by Entry Time (`sort_by_entry_time`):** Reorders the vehicles chronologically based on their entry time. This demonstrates algorithm implementation within the constraints of the ADT.

## 5. Big-O Analysis Summary
The core operations of the system exhibit the following time complexities, where **N** is the number of currently parked vehicles:

*   **Park a Vehicle (Average Case: O(N)):** Before adding a new vehicle, the system must iterate through the existing vehicles to check for duplicate license plates, requiring an O(N) scan. The actual addition to the internal list is O(1).
*   **Remove a Vehicle (Worst Case: O(N)):** To remove a vehicle, the system must perform a linear search to find the matching license plate. Once found, removing the item from the list also takes O(N) time because subsequent elements must be shifted.
*   **Search for a Vehicle (Worst Case: O(N)):** Searching by license plate requires a linear traversal of the parked vehicles until the matching plate is found or the end of the list is reached.
*   **Check Availability (O(1)):** Calculating the remaining spots involves simple arithmetic: subtracting the current size of the list (an O(1) operation) from the fixed capacity.
*   **Sort by Entry Time (O(N log N)):** The sorting operation relies on Python's built-in Timsort algorithm, which guarantees a worst-case time complexity of O(N log N).

## 6. Testing Overview
The project relies on a comprehensive suite of automated tests to guarantee the reliability of the system.

*   **Framework:** Testing is strictly implemented using Python's built-in `unittest` module. No external testing frameworks are utilized, keeping the project dependencies minimal.
*   **Scope:**
    *   **Unit Tests:** Individual ADTs (`Vehicle`, `SimpleList`, `ParkingLot`) are tested in isolation to verify their initialization, state management, and basic operations.
    *   **Integration/System Tests:** The `TestParkingSystem` class verifies that the components interact correctly. It covers complete workflows, such as parking multiple vehicles, reaching capacity, and removing vehicles.
*   **Coverage:** The tests specifically address normal usage scenarios (e.g., successful parking), edge cases (e.g., removing from an empty lot, adding to a full lot), invalid inputs (e.g., attempting to park a non-vehicle object), and duplicate handling.
*   **Feedback:** The tests print clearly labeled results to the console during execution, providing immediate and understandable feedback on the system's health.
