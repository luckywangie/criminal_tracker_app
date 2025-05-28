from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Criminal, Crime, Category
from datetime import date

# Database connection setup
engine = create_engine("sqlite:///criminal_tracker.db")
Session = sessionmaker(bind=engine)
session = Session()

# removes data before seeding to avoid repetition and duplicity
session.query(Crime).delete()
session.query(Criminal).delete()
session.query(Category).delete()

# Crime Categories
robbery = Category(name="Robbery")
hostage = Category(name="Hostage Situation")
cybercrime = Category(name="Cybercrime")
fraud = Category(name="Fraud")
session.add_all([robbery, hostage, cybercrime, fraud])
session.commit()

# Criminals inspired by moneyheist
professor = Criminal(
    name="Sergio Marquina",
    alias="The Professor",
    gender="Male",
    date_of_birth=date(1975, 4, 10)
)

tokyo = Criminal(
    name="Silene Oliveira",
    alias="Tokyo",
    gender="Female",
    date_of_birth=date(1989, 11, 18)
)

berlin = Criminal(
    name="Andrés de Fonollosa",
    alias="Berlin",
    gender="Male",
    date_of_birth=date(1973, 6, 2)
)

nairobi = Criminal(
    name="Ágata Jiménez",
    alias="Nairobi",
    gender="Female",
    date_of_birth=date(1985, 5, 14)
)

session.add_all([professor, tokyo, berlin, nairobi])
session.commit()

# Crimes committed
crime1 = Crime(
    title="Heist at the Royal Mint",
    description="Planned and led the printing of billions of euros from inside the Royal Mint of Spain.",
    date=date(2019, 5, 1),
    location="Madrid, Spain",
    severity="High",
    criminal_id=professor.id,
    category_id=fraud.id
)

crime2 = Crime(
    title="Bank of Spain Takeover",
    description="Participated in the seizure of the Bank of Spain, taking hostages and accessing national gold reserves.",
    date=date(2021, 1, 15),
    location="Madrid, Spain",
    severity="High",
    criminal_id=tokyo.id,
    category_id=hostage.id
)

crime3 = Crime(
    title="Transport of Hostages",
    description="Managed hostage movement and public negotiations during the Royal Mint operation.",
    date=date(2019, 5, 3),
    location="Madrid, Spain",
    severity="Medium",
    criminal_id=berlin.id,
    category_id=hostage.id
)

crime4 = Crime(
    title="Forgery of Currency",
    description="Oversaw the printing of €2.4 billion in untraceable currency.",
    date=date(2019, 5, 6),
    location="Madrid, Spain",
    severity="Medium",
    criminal_id=nairobi.id,
    category_id=robbery.id
)

session.add_all([crime1, crime2, crime3, crime4])
session.commit()

print("Database seeded successfully!.")
