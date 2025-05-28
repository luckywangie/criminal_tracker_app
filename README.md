# 🔍 Criminal Tracker CLI App

This is a simple, terminal-based application designed to help users manage records related to criminals, the crimes they’ve committed, and the categories those crimes fall under. It uses Python with SQLAlchemy for database operations and includes Alembic for handling schema migrations.

---

##  What The App Does

The Criminal Tracker allows you to:

- Register and view criminals
- Create and manage crime categories (e.g., Robbery, Cybercrime)
- Record crimes and associate them with specific criminals and categories
- Update or delete entries across all tables
- Seed the database 

---

## Tech used

- **Python**
- **SQLAlchemy** – ORM for handling database logic
- **SQLite** – lightweight, file-based database
- **Alembic** – for database migrations
- **CLI** – fully interactive via terminal input

---

## Project Structure
criminal_tracker_app/
 App/
  main.py # Main application logic & menu
  models.py # SQLAlchemy models for Criminal, Crime, and Category
  seed.py # Seeds the database with test data
criminal_tracker.db # The SQLite database file
│
alembic/ # Alembic migration scripts
 env.py
 versions
 __pycache__
README.md # You're here!

## Getting started
1. Clone the repository
2. Install required packages/dependencies
3. Run database migrations
4. Seed database
5. Run the app (
  cd App
  python main.py
)
6. Interact with the app via the terminal
---
