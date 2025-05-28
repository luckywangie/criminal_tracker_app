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
   gitclone https://github.com/luckywangie/criminal_tracker_app
2. Install required packages/dependencies
   pipnev install
     python
     sqlalchemy
     alembic

3. Run database migrations
   alembic upgrade head
4. Seed database
5. Run the app (
  cd App
  python main.py
)
6. Interact with the app via the terminal
---

## Author
Lucky Mamati

## License
Copyright --- 2025 Lucky Mamati

Permission is hereby granted , free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
---