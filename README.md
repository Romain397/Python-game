# Python-game
This program helps manage a fleet of spaceships, allowing you to add/remove ships and crew, track ship readiness, and view statistics. It features random events like enemy attacks or reinforcements. Data can be saved and loaded from JSON files for easy persistence and management of the fleet's status.

# Fleet Management System

**Fleet Management System** is a Python-based console game that allows you to manage a fleet of spaceships. Each spaceship is equipped with a crew, and each member has a unique role such as pilot, technician, or mentalist. You can add crew members, check the readiness of spaceships, save and load the fleet's state in JSON format, and deal with random events like enemy attacks and reinforcements.

## Features

- **Manage your fleet**: Create and rename a fleet, add and remove spaceships, and manage crew members.
- **Crew management**: Add crew members with different roles (pilot, technician, mentalist) and track their experience and mana.
- **Spaceship readiness**: Check if a spaceship is ready for battle or in need of repairs.
- **Random events**: Encounter random events like enemy attacks and reinforcements that can affect the fleet.
- **Save and load**: Save the current state of your fleet to a file and load it later.

## Setup

To run this game, simply clone the repository and run the Python script `fleet_management.py`.

```bash
git clone <repository_url>
cd FleetManagement
python fleet_management.py

How to Play
Choose options from the menu to manage your fleet, add members, check ship conditions, and more.

Random events will occur during the game, adding an element of surprise.

Save and load your progress by entering the file name where you want to store the fleet's data.

Sample Menu

=== Fleet Management ===
1. Rename the fleet
2. Add a spaceship
3. Add a crew member
4. Remove a crew member
5. Display crew information
6. Check a spaceship's readiness
7. Show fleet statistics
8. Show detailed statistics
9. Save fleet data
10. Load fleet data
11. Exit

Requirements
Python 3.x

Standard Python libraries (json, ast, random)

License
This project is open source and available under the MIT License. See the LICENSE file for more information.

Code Explanation:
Fleet, Spaceship, and Operator are classes you have defined to represent a fleet of spaceships, each spaceship, and the crew members respectively.

Saving and loading data: The code allows you to save the state of the fleet into a JSON file and load it at any time.

Random events: There are events like enemy attacks or reinforcements that can affect the state of the fleet.

Crew member management: You can add and remove crew members, and display their specific information.
