# Finance Manager

Welcome to the **Finance Manager**!

This Python program helps you manage your monthly income, record your expenses, and provides a financial summary with insights on your spending habits.

---

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [File Storage](#file-storage)
- [Contact Information](#contact-information)
- [License](#license)

---

## Features

- **Income Input**: Enter your monthly income.
- **Expense Tracking**: Record expenses with categories and amounts.
- **Expense Summation**: Calculates total expenses.
- **Balance Calculation**: Computes remaining balance after expenses.
- **Financial Summary**: Provides a summary of income, expenses, and balance.
- **Spending Feedback**: Gives feedback based on your spending habits.
- **Data Persistence**: Saves expenses to a JSON file for future reference.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/NnannaMari09033/finance_manager.git
   cd finance_manager


Install Dependencies

If your program requires any external libraries, list them here. If not, you can omit this step.

Usage
Run the Program

bash
python finance_manager.py
Follow the Prompts

Enter your monthly income when prompted.
Choose to enter expenses or indicate you are done.
Input your expense categories and amounts.
View the financial summary and feedback provided by the program.
File Storage
Expenses are saved to json_store/mobiles.json for future reference. Ensure that this directory exists and is writable.

Contact Information
For any inquiries or suggestions, feel free to reach out:

Name: Mari Nnanna
Email: nnannamari@gmail.com

License
This project is licensed under the MIT License.

Thank you for using the Finance Manager! We hope it helps you manage your finances effectively.






# Social Event Organizer

**Author**: Mari Nnanna  
**Contact**: nnannamari@gmail.com

## Description

The `SocialEventOrganizer` is a Python class designed to help organize and manage social events. The class allows users to:

- Create events with essential details such as the organizer's name, age, gender, and event information.
- View a list of all upcoming events.
- Search for a specific event by its title.
- Cancel an event.
- Store and retrieve events from a file to ensure persistence.

## Features

### 1. Create Event
Users can create new social events by providing the following details:

- **Event Title**: A brief title for the event.
- **Organizer's Name**: Name of the person organizing the event.
- **Organizer's Age**: The age of the event organizer.
- **Organizer's Gender**: The gender of the organizer (M/F).
- **Event Date**: Date of the event (in `YYYY-MM-DD` format).
- **Event Location**: The venue or location of the event.
- **Maximum Number of Attendees**: The total number of people allowed at the event.

### 2. View All Events
Users can view all the events that have been added to the system. If there are no events, a message will indicate that no events are available.

### 3. Search Event by Title
The user can search for an event by its title and retrieve detailed information, including the organizer's name, age, gender, and event specifics.

### 4. Cancel Event
If an event needs to be canceled, users can delete it by providing the event's title.

### 5. File Persistence
The class supports file-based storage, allowing events to be saved to and loaded from a JSON file. This ensures that all event data is retained between program executions.

## Example Usage

```python
# Usage of the SocialEventOrganizer class
ma = SocialEventOrganizer()
ma.user_choice()
This will prompt the user to interact with the system, allowing them to create, view, search, and cancel events.

Dependencies
JSON file for storing event data: another_store/event.json

File Structure
Ensure you have the following file structure:
bash
├── another_store/
│   └── event.json  # Stores event data
├── SocialEventOrganizer.py  # Main Python script