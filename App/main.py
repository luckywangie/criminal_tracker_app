from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from App.models import Criminal, Crime, Category
from datetime import date

#connection to database
engine = create_engine("sqlite:///criminal_tracker.db")
Session = sessionmaker(bind=engine)
session = Session()

# Criminal functions
#create a criminal
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
#list all criminals
def list_criminals():
    criminals = session.query(Criminal).all()
    for c in criminals:
        print(f"ID: {c.id}, Name: {c.name}, Alias: {c.alias}, DOB: {c.date_of_birth}")
#view criminal by ID
def view_criminal_by_id():
    cid = input("Enter criminal ID: ")
    criminal = session.query(Criminal).get(cid)
    if criminal:
        print(f"ID: {criminal.id}, Name: {criminal.name}, Alias: {criminal.alias}, Gender: {criminal.gender}, DOB: {criminal.date_of_birth}")
    else:
        print("Criminal not found.")
#update a criminal
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
#delete a criminal
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
#add a category
def create_category():
    name = input("New category name: ")
    if session.query(Category).filter_by(name=name).first():
        print("Category already exists.")
        return
    session.add(Category(name=name))
    session.commit()
    print("Category created.")
#list all categories
def list_categories():
    categories = session.query(Category).all()
    for cat in categories:
        print(f"ID: {cat.id}, Name: {cat.name}")
#view a category by ID
def view_category_by_id():
    cid = input("Enter category ID: ")
    category = session.query(Category).get(cid)
    if category:
        print(f"ID: {category.id}, Name: {category.name}")
    else:
        print("Category not found.")
#update a category
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
#delete a category
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

#Crime functions
#record a crime
def record_crime():
    title = input("Crime title: ")
    description = input("Description: ")
    location = input("Location: ")
    severity = input("Severity (Low/Medium/High): ")
    crime_date = date(
        int(input("Year: ")),
        int(input("Month: ")),
        int(input("Day: "))
    )

    list_criminals()
    criminal_id = int(input("Criminal ID: "))
    list_categories()
    category_id = int(input("Category ID: "))

    crime = Crime(
        title=title,
        description=description,
        date=crime_date,
        location=location,
        severity=severity,
        criminal_id=criminal_id,
        category_id=category_id
    )
    session.add(crime)
    session.commit()
    print("Crime recorded.")
#list all crimes comitted
def list_crimes():
    crimes = session.query(Crime).all()
    for c in crimes:
        print(f"ID: {c.id}, Title: {c.title}, Severity: {c.severity}, Location: {c.location}, Date: {c.date}")
#view a crime by ID
def view_crime_by_id():
    cid = input("Enter crime ID: ")
    crime = session.query(Crime).get(cid)
    if crime:
        print(f"Title: {crime.title}, Description: {crime.description}, Date: {crime.date}, Location: {crime.location}, Severity: {crime.severity}")
    else:
        print("Crime not found.")
#update a crime
def update_crime():
    crime_id = input("Enter crime ID to update: ")
    crime = session.query(Crime).get(crime_id)
    if not crime:
        print("Crime not found.")
        return

    print("Leave a field empty to keep the current value.")
    title = input(f"New title (current: {crime.title}): ") or crime.title
    description = input(f"New description (current: {crime.description}): ") or crime.description
    location = input(f"New location (current: {crime.location}): ") or crime.location
    severity = input(f"New severity (current: {crime.severity}): ") or crime.severity

    change_date = input("Change crime date? (y/n): ")
    if change_date.lower() == 'y':
        year = int(input("Year: "))
        month = int(input("Month: "))
        day = int(input("Day: "))
        crime.date = date(year, month, day)

    change_criminal = input("Change associated criminal? (y/n): ")
    if change_criminal.lower() == 'y':
        list_criminals()
        crime.criminal_id = int(input("New Criminal ID: "))

    change_category = input("Change crime category? (y/n): ")
    if change_category.lower() == 'y':
        list_categories()
        crime.category_id = int(input("New Category ID: "))

    crime.title = title
    crime.description = description
    crime.location = location
    crime.severity = severity

    session.commit()
    print("Crime updated successfully.")
#delete a crime 
def delete_crime():
    cid = input("Enter crime ID to delete: ")
    crime = session.query(Crime).get(cid)
    if crime:
        confirm = input(f"Delete {crime.title}? (y/n): ")
        if confirm.lower() == 'y':
            session.delete(crime)
            session.commit()
            print("Crime deleted.")
    else:
        print("Crime not found.")

#MAIN MENU
def main():
    while True:
        print("\n======= CRIMINAL TRACKER MENU =======")
        print(" [ Criminals ]")
        print("1. Add Criminal")
        print("2. List All Criminals")
        print("3. View Criminal by ID")
        print("4. Update Criminal by ID")
        print("5. Delete Criminal")

        print("\n [ Crime Categories ]")
        print("6. Create Crime Category")
        print("7. List All Categories")
        print("8. View Category by ID")
        print("9. Update Category by ID")
        print("10. Delete Category")

        print("\n [ Crimes ]")
        print("11. Record New Crime")
        print("12. List All Crimes")
        print("13. View Crime by ID")
        print("14. Update Crime by ID")
        print("15. Delete Crime by ID")

        print("\n0. Exit")

        choice = input("\nYour choice: ").strip()
        if choice == "1":
            create_criminal()
        elif choice == "2":
            list_criminals()
        elif choice == "3":
            view_criminal_by_id()
        elif choice == "4": 
            update_criminal()
        elif choice == "5":
            delete_criminal()
        elif choice == "6": 
            create_category()
        elif choice == "7": 
            list_categories()
        elif choice == "8": 
            view_category_by_id()
        elif choice == "9": 
            update_category()
        elif choice == "10": 
            delete_category()
        elif choice == "11": 
            record_crime()
        elif choice == "12": 
            list_crimes()
        elif choice == "13": 
            view_crime_by_id()
        elif choice == "14":
            update_crime()
        elif choice == "15": 
            delete_crime()
       
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

