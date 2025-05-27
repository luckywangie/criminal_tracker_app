from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from App.models import Criminal, Crime, Category
from datetime import date

#connection to database
engine = create_engine("sqlite:///criminal_tracker.db")
Session = sessionmaker(bind=engine)
session = Session()

# Criminal functions
def create_criminal():
    name = input("Enter the name of the criminal: ")
    alias = input("Enter the alias of the criminal: ")
    gender = input("Enter the gender of the criminal: ")
    
    dob = date(
        int(input("Enter the year of birth: ")),
        int(input("Enter the month of birth: ")),
        int(input("Enter the day of birth: "))
    )

    criminal = Criminal(name=name, alias=alias, gender=gender, date_of_birth=dob)
    session.add(criminal)
    session.commit()
    print("Criminal created successfully")

def list_criminals():
    criminals = session.query(Criminal).all()
    for c in criminals:
        print(f"ID: {c.id}, Name: {c.name}, Alias: {c.alias}, DOB: {c.date_of_birth}")

def view_criminal_by_id():
    cid = input("Enter criminal ID: ")
    criminal = session.query(Criminal).get(cid)
    if criminal:
        print(f"ID: {criminal.id}, Name: {criminal.name}, Alias: {criminal.alias}, Gender: {criminal.gender}, DOB: {criminal.date_of_birth}")
    else:
        print("Criminal not found.")

def update_criminal():
    cid = input("Enter criminal ID to update: ")
    criminal = session.query(Criminal).get(cid)
    if criminal:
        print("Leave a field empty to keep current value.")
        name = input(f"New name (current: {criminal.name}): ") or criminal.name
        alias = input(f"New alias (current: {criminal.alias}): ") or criminal.alias
        gender = input(f"New gender (current: {criminal.gender}): ") or criminal.gender
        criminal.name, criminal.alias, criminal.gender = name, alias, gender
        session.commit()
        print("Criminal updated.")
    else:
        print("Criminal not found.")

def delete_criminal():
    cid = input("Enter criminal ID to delete: ")
    criminal = session.query(Criminal).get(cid)
    if criminal:
        confirm = input(f"Delete {criminal.name}? (y/n): ")
        if confirm.lower() == 'y':
            session.delete(criminal)
            session.commit()
            print("Criminal deleted.")
    else:
        print("Criminal not found.")

#Category functions
def create_category():
    name = input("New category name: ")
    if session.query(Category).filter_by(name=name).first():
        print("Category already exists.")
        return
    session.add(Category(name=name))
    session.commit()
    print("Category created.")

def list_categories():
    categories = session.query(Category).all()
    for cat in categories:
        print(f"ID: {cat.id}, Name: {cat.name}")

def view_category_by_id():
    cid = input("Enter category ID: ")
    category = session.query(Category).get(cid)
    if category:
        print(f"ID: {category.id}, Name: {category.name}")
    else:
        print("Category not found.")

def update_category():
    cid = input("Enter category ID to update: ")
    category = session.query(Category).get(cid)
    if category:
        new_name = input(f"New name (current: {category.name}): ")
        if new_name:
            category.name = new_name
            session.commit()
            print("Category updated.")
    else:
        print("Category not found.")

def delete_category():
    cid = input("Enter category ID to delete: ")
    category = session.query(Category).get(cid)
    if category:
        confirm = input(f"Delete {category.name}? (y/n): ")
        if confirm.lower() == 'y':
            session.delete(category)
            session.commit()
            print("Category deleted.")
    else:
        print("Category not found.")