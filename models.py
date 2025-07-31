from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# The base class for all ORM models
Base = declarative_base()


# Address table/entity
class Address(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True)
    street = Column(String)
    number = Column(Integer)
    county = Column(String)
    country = Column(String)
    eircode = Column(String)


# User table/entity
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    age = Column(Integer)
    address_id = Column(Integer, ForeignKey("addresses.id"))
    address = relationship("Address")


# Create the SQLite DB and tables
engine = create_engine("postgresql+psycopg2://postgres:yourpassword@localhost:5432/postgres")
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(bind=engine)
