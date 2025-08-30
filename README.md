# CLI Contribution Tracker

This is a **CLI (Command-Line Interface)** and **ORM (Object-Relational Mapper)** application built in Python. It's designed to solve the real-world problem of tracking contributions from various individuals to an organization. The project demonstrates core software development practices, including database management, modular design, and user interaction through a command-line interface.


### Learning Goals

This project was developed to achieve several key learning goals:

  * **CLI Application Design**: The application uses a well-structured CLI to provide a user-friendly way to interact with the system without a graphical interface.
  * **SQLAlchemy ORM**: It utilizes SQLAlchemy to create and manage a database. This demonstrates how to interact with a database using Python objects instead of raw SQL queries, making the code more readable and maintainable. The application features three interconnected tables (`organizations`, `contributors`, and `contributions`), showcasing a **one-to-many relationship**.
  * **Modular Code Structure**: The project adheres to best practices by organizing the code into logical directories (`lib/`, `models/`, etc.). This separation of concerns improves readability and makes the code easier to debug and extend.
  * **Data Structures**: The application effectively uses Python's built-in data structures, such as **lists**, **dicts**, and **tuples**, to handle and manipulate data retrieved from the database or provided by the user.



### Getting Started

#### Prerequisites

  * Python 3.6 or newer.
  * The **SQLAlchemy** library.

#### Installation

1.  **Clone or download** the project files.
2.  **Navigate** to the project's root directory in your terminal.
3.  **Install the required library** using `pip`:
    ```bash
    pip install sqlalchemy
    ```



### Usage

1.  **Run the application** from the project's root directory:
    ```bash
    python3 main.py
    ```
2.  The program will automatically create a **SQLite database file** named `contributions.db` on its first run.
3.  Use the **on-screen menus** to add, view, and manage organizations, contributors, and their contributions.



### Technical Communication

The project's code is well-commented and its structure is logical, making it easy to understand the technical concepts behind it. The use of an ORM simplifies database interactions, allowing for clear and concise code when performing CRUD (Create, Read, Update, Delete) operations. The menu-driven CLI provides a direct and accurate demonstration of the application's functionality.