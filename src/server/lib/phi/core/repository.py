#!/usr/bin/env python
# encoding: utf-8
'''
repository.py

Created by Rodolfo Barriga
'''
import phi.core.model as model

class Base:

	def __init__(self, session):
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

class User(Base):
	entity = model.User
	
	def search_count(self, user_name, name, last_name, group_id, role_id):
		query = self._build_base_query(user_name, name, last_name, group_id, role_id)
		return query.count()

	def search(self, user_name, name, last_name, group_id, role_id, start, limit):
		query = self._build_base_query(user_name, name, last_name, group_id, role_id)
		query = query.limit(limit) \
		.offset(start)

		return query.all()
	
	def _build_base_query(self, user_name, name, last_name, group_id, role_id):
		query = self.session.query(self.entity) \
		.filter(self.entity.user_name.like(user_name)) \
		.filter(self.entity.name.like(name)) \
		.filter(self.entity.last_name.like(last_name))
		
		if(role_id != 0):
			query = query.join(self.entity.roles) \
			.filter(model.Role.id == role_id)
		
		if(group_id != 0):
			query = query.join(self.entity.groups) \
			.filter(model.Group.id == group_id)
		
		return query
		
class Location(Base):
	entity = model.Location

class Workspace(Base):
	entity = model.Workspace
		
	def get_by_owner(self, user_name):
		return self.session.query(self.entity).filter(self.entity.user_name==user_name).all()

class Node(Base):
	entity = model.Node

class Layer(Base):
	entity = model.Layer

class Raster(Base):
	entity = model.Raster

class Role(Base):
	entity = model.Role

class Group(Base):
	entity = model.Group
