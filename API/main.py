from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

# Database URL - update it to your MySQL connection details
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://admin:CSC394!!@database-1.cn0geogwil7k.us-east-2.rds.amazonaws.com/ChubbyHotels"

# Create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our model
Base = declarative_base()

# Define the Properties table model
class Property(Base):
    __tablename__ = 'Properties'

    PropertyID = Column(Integer, primary_key=True, index=True)
    Name = Column(String(100), nullable=False)
    Country = Column(String(50), nullable=False)
    City = Column(String(50), nullable=False)
    ImageLocation = Column(String(255), nullable=False)
    IsChubby = Column(Boolean, default=False)
    IsActive = Column(Boolean, default=True)

# FastAPI instance
app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (use more restrictive settings in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to get all properties
@app.get("/properties/")
def get_properties(db: Session = Depends(get_db)):
    properties = db.query(Property).all()  # Query all properties
    return properties

# Route to get a specific property by ID
@app.get("/properties/{property_id}")
def get_property(property_id: int, db: Session = Depends(get_db)):
    property = db.query(Property).filter(Property.PropertyID == property_id).first()  # Get specific property by ID
    if property is None:
        return {"message": "Property not found"}
    return property