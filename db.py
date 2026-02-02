from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


URI = 'postgresql://postgres:12345678@localhost:5432/postgres'
engine = create_engine(URI)
Session = sessionmaker(bind=engine)
session = Session()