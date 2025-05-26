from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

#creats base cls used by all models
Base = declarative_base()

#for person commiting the crime
class Criminal(Base):
    __tablename__ = 'criminals'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    alias = Column(String(100))
    gender = Column(String(10))
    date_of_birth = Column(DateTime)

#relationship one criminal can perform many crimes
    crimes = relationship("Crime", back_populates="criminal", cascade="all, delete-orphan")

#for grouping same crimes
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

#relationship one category has many crimes
    crimes = relationship("Crime", back_populates="category")

#for a specific crime committed
class Crime(Base):
    __tablename__ = 'crimes'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
    date = Column(DateTime, nullable=False)
    location = Column(String(100), nullable=False)
    severity = Column(String(20), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

#foreign key for linking crime to a specific criminal
    criminal_id = Column(Integer, ForeignKey("criminals.id"), nullable=False)

#foreign key for crime to a specific crime category
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

#relationships to our criminal and category models
    criminal = relationship("Criminal", back_populates="crimes")
    category = relationship("Category", back_populates="crimes")
