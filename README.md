# Study Abroad Planner

## Description
Study Abroad Planner is a Python application designed to help students organize and manage their study abroad application process.
Preparing to study abroad can be a long and complicated process. Students usually need to search for universities, choose their preferred institutions, prepare language certificates and other required documents, and keep track of their application progress. Managing all of this information can become confusing, especially when applying to multiple universities.
This project provides a simple command-line application that helps users organize all of these tasks in one place.
The program allows users to create a personal application profile by entering their name, destination country, selected universities, intended major, and required application documents. Users can save their profile and continue editing it whenever they return without losing their previous progress.
The application supports the following features:
- Search for a destination country using stored JSON data.
- Display available universities in the selected country.
- Select preferred universities for the application.
- Create a personalized study abroad profile.
- Add required application documents and certificates.
- Mark completed documents.
- Add new documents later.
- Remove unnecessary documents.
- Track completed and remaining documents.
- Calculate the application readiness percentage.
- Save the user's profile.
- Load a previously saved profile and continue editing it.
- Handle invalid user input without crashing.
The main goal of this project is to make the study abroad preparation process more organized, easier to manage, and less stressful for students planning to apply to international universities.
---
## Features
### Country Search
Users can search for their destination country using country data stored in a JSON file. Partial matching is supported, making it easier to find countries.
### University Selection
After selecting a country, the program searches available universities stored in another JSON file. Users can search by university name and choose their preferred universities for their application.
### Application Profile
Users create a personal application profile containing:
- Name
- Destination country
- Selected universities
- Intended major
- Required application documents
### Document Management
Users can:
- Add new documents
- Remove documents
- Mark documents as completed
- View completed documents
- View remaining documents
### Progress Tracking
The program automatically calculates the user's application readiness percentage based on completed documents.
### Save and Load
The application saves user information into a JSON file.
When the program is opened again, the previous profile can be loaded automatically, allowing users to continue managing their application without starting from the beginning.
### Error Handling
The program validates user input and handles invalid options gracefully by displaying helpful error messages instead of terminating unexpectedly.
---
## Project Files
### project.py
Contains the main application, including:
- Studentp class
- Country search
- University selection
- Profile management
- Document management
- Saving and loading profiles
### test_project.py
Contains automated tests written using pytest to verify the main functionality of the application.
### countries.json
Stores country information used by the country search feature.
### universities.json
Stores university information used for university selection.
### requirements.txt
Lists the external Python packages required to run the project.
---
## Technologies Used
- Python 3
- Object-Oriented Programming (OOP)
- JSON
- Pytest
---
## How to Run
Install the required packages:
pip install -r requirements.txt

Run the application:
python project.py

Run the tests:
python -m pytest test_project.py

---
## Notes
This project was developed as the final project for CS50's Introduction to Programming with Python (CS50P).