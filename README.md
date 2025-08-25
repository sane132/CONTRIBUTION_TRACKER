# Contribution Tracking System

A command-line application for tracking contributions from members, volunteers, and donors of an organization.

## Features

- Manage organizations, contributors, and contributions
- Track contributions with dates, amounts, and notes
- Generate reports on contributions by type and date range
- Create thank you messages for contributors
- Data persistence using SQLite database

## Installation

1. Clone this repository
2. Install dependencies: `pipenv install`
3. Activate the virtual environment: `pipenv shell`
4. Run the application: `python debug.py`

## Usage

The application provides a menu-driven interface with the following options:

1. **Manage Contributors**: View, add, find, or delete contributors
2. **Manage Contributions**: View, add, find, or delete contributions
3. **View Reports**: Generate reports on contributions by type or date range
4. **Thank Contributors**: Generate thank you messages for recent contributors
5. **Exit**: Exit the application

## Data Model

The application uses three main models:

1. **Organization**: Represents the organization receiving contributions
2. **Contributor**: Represents individuals who contribute (members, volunteers, donors)
3. **Contribution**: Represents individual contributions with amount, date, and notes

## Relationships

- An Organization has many Contributors (one-to-many)
- A Contributor has many Contributions (one-to-many)

## Validation

The application includes validation for:
- Contributor type (must be member, volunteer, or donor)
- Contribution amount (must be greater than 0)
- Date format validation
- Input type validation for numbers and dates