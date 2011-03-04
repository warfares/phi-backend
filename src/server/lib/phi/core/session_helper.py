#!/usr/bin/env python
# encoding: utf-8
'''
session_helper.py

Created by Rodolfo Barriga 
'''
from sqlalchemy import orm
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

def create_main_engine():
	engine = create_engine('postgresql://postgres:postgres@localhost/phi')
	engine.echo = False
	return engine

def create_session():
	
	# Set up the session
	engine = create_main_engine()
	sm = orm.sessionmaker(bind=engine, autoflush=True, expire_on_commit=True)
	
	#scope_session different session is used for each thread 
	#so that every request can have its own access to the database.
	session = orm.scoped_session(sm)
	return session