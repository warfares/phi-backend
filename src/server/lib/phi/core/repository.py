#!/usr/bin/env python
# encoding: utf-8
'''
repository.py

Created by Rodolfo Barriga
'''
import phi.core.model as model

class Base:

	def __init__(self, entity, session = ''):
		self.entity = entity
		self.session = session

	def all(self):
		list = self.session.query(self.entity).all()
		return list

	def read(self, id):
		return self.session.query(self.entity).get(id)

	def create_update(self, obj):
		self.session.add(obj)
		self.session.commit()
		return True
		
	def delete(self, obj):
		self.session.delete(obj)
		self.session.commit()
		return True

#child class

class User(Base):
	def __init__(self, session):
		self.session = session
		self.entity = model.User
	
	def search_count(self, user_name, name, last_name, group_id, role_id):
		total = self.session.query(self.entity) \
		.filter(self.entity.user_name.like(user_name)) \
		.filter(self.entity.name.like(name)) \
		.filter(self.entity.last_name.like(last_name)) \
		.count()
		return total
	
	def search(self, user_name, name, last_name, group_id, role_id, start, limit):
		query = self.session.query(self.entity) \
		.filter(self.entity.user_name.like(user_name)) \
		.filter(self.entity.name.like(name)) \
		.filter(self.entity.last_name.like(last_name)) \
		.all()
		return query
	
class Location(Base):
	def __init__(self, session):
		self.session = session
		self.entity = model.Location


class Workspace(Base):
	def __init__(self, session):
		self.session = session
		self.entity = model.Workspace
		
	def get_by_owner(self, user_name):
		return self.session.query(self.entity).filter(self.entity.user_name==user_name).all()


class Node(Base):
	def __init__(self, session):
		self.session = session
		self.entity = model.Node


class Layer(Base):
	def __init__(self, session):
		self.session = session
		self.entity = model.Layer


class Raster(Base):
	def __init__(self, session):
		self.session = session
		self.entity = model.Raster


class Role(Base):
	def __init__(self, session):
		self.session = session
		self.entity = model.Role


class Group(Base):
	def __init__(self, session):
		self.session = session
		self.entity = model.Group
