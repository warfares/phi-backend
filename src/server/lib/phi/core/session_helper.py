#!/usr/bin/env python
# encoding: utf-8
"""
session_helper.py

Created by Rodolfo Barriga 
"""
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

def create_main_engine():
	engine = create_engine('postgresql://postgres:postgres@localhost/phi')
	engine.echo = False
	return engine

def create_session():
	engine = create_main_engine()
	Session = sessionmaker(bind=engine)
	return Session()