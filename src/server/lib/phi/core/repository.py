#!/usr/bin/env python
# encoding: utf-8
'''
repository.py

Created by Rodolfo Barriga
'''
import phi.core.model as model

class Base:

	def __init__(self, entity, session):
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


class User(Base):
	def __init__(self, session):
		self.session = session
		self.entity = model.User
	
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
