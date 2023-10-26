import json
from sqlalchemy import create_engine
from model import Coffee, Base
from sqlalchemy.orm import sessionmaker
from flask import jsonify

engine = create_engine("sqlite:///coffee.db?check_same_thread=False")
Base.metadata.create_all(engine)

# Connect to the database
Session = sessionmaker(bind=engine)
session = Session()



def read():
	coffee = session.query(Coffee).all()

	return jsonify(coffee=[c.serialize() for c in coffee])