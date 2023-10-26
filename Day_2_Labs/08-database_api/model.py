from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from dataclasses import dataclass

Base = declarative_base()

@dataclass
class Coffee(Base):
    __tablename__ = "coffee"

    id = Column(Integer, primary_key=True)
    coffee_name = Column(String, unique=True)
    milk = Column(String)
    timestamp = Column(DateTime)


    def serialize(self):
        return {
            'id': self.id,
            'coffee_name': self.coffee_name,
            'milk': self.milk,
            'timestamp': self.timestamp
        }