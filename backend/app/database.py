from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///plagiarism.db")
Session = sessionmaker(bind=engine)
session = Session()

class PlagiarismCheck(Base):
    __tablename__ = "plagiarism_results"
    id = Column(Integer, primary_key=True)
    file_name = Column(String)
    similarity_score = Column(Float)
    result = Column(String)  # "Plagiarized" or "Unique"

def init_db():
    Base.metadata.create_all(engine)
