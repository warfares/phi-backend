#!/usr/bin/env python
# encoding: utf-8
'''
model.py

Created by Rodolfo Barriga
'''
from sqlalchemy import Table, Column, ForeignKey, String, Integer, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from geoalchemy import *

Base = declarative_base()

#user many-to-many relations
user_nodes = Table('app_user_node', Base.metadata,
	Column('user_name', String, ForeignKey('app_user.user_name')),
	Column('app_node_id', Integer, ForeignKey('app_node.id'))
)

user_rasters = Table('app_user_raster', Base.metadata,
	Column('user_name', String, ForeignKey('app_user.user_name')),
	Column('app_raster_id', Integer, ForeignKey('app_raster.id'))
)

user_locations = Table('app_user_location', Base.metadata,
	Column('user_name', String, ForeignKey('app_user.user_name')),
	Column('location_id', Integer, ForeignKey('app_location.id'))
)

user_workspaces = Table('app_user_workspace', Base.metadata,
	Column('user_name', String, ForeignKey('app_user.user_name')),
	Column('workspace_id', Integer, ForeignKey('app_workspace.id'))
)

user_groups = Table('app_user_group', Base.metadata,
	Column('user_name', String, ForeignKey('app_user.user_name')),
	Column('app_group_id', Integer, ForeignKey('app_group.id'))
)

user_roles = Table('app_user_role', Base.metadata,
	Column('user_name', String, ForeignKey('app_user.user_name')),
	Column('app_role_id', Integer, ForeignKey('app_role.id'))
)

layer_files = Table('app_layer_file', Base.metadata,
	Column('layer_name', String, ForeignKey('app_layer.name')),
	Column('file_id', Integer, ForeignKey('app_file.id'))
)


class User(Base):
	__tablename__ = 'app_user'

	user_name = Column(String, primary_key=True)
	name = Column(String)
	last_name = Column(String)
	email = Column(String)
	enabled = Column(String)
	password = Column(String)
	
	nodes = relationship('Node', secondary=user_nodes, backref='app_user')
	rasters = relationship('Raster', secondary=user_rasters, backref='app_user')
	locations = relationship('Location', secondary=user_locations, backref='app_user')
	workspaces = relationship('Workspace', secondary=user_workspaces, backref='app_user')
	groups = relationship('Group', secondary=user_groups, backref='app_user')
	roles = relationship('Role', secondary=user_roles, backref='app_user')
	
	def __repr__(self):
		return "<User('%s','%s', '%s')>" % (self.user_name, self.name, self.last_name)

class Layer(Base):
	__tablename__ = 'app_layer'

	name = Column(String, primary_key=True)
	project = Column(String)
	title = Column(String)
	type = Column(String)
	date = Column(Date)
	srid = Column(String)
	files = relationship('File', secondary=layer_files, backref='app_layer')

	def __repr__(self):
		return "<Layer('%s','%s','%s')>" % (self.name, self.type, self.srid)

class Node(Base):
	__tablename__ = 'app_node'
	id = Column(Integer, primary_key=True)
	parent_id = Column(Integer)
	description = Column(String)
	order = Column(Integer)
	leaf = Column(Boolean)
	layer_id = Column(String, ForeignKey('app_layer.name'))
	layer = relationship(Layer, backref='app_layer')

	def __repr__(self):
		return "<Node('%s','%s')>" % (self.id, "10")

class Raster(Base):
	__tablename__ = 'app_raster'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	description = Column(String)
	visible = Column(Boolean)
	url = Column(String)
	minz = Column(Integer)
	maxz = Column(Integer)
	point = GeometryColumn(Point(2,96))
	min = GeometryColumn(Point(2,96))
	max = GeometryColumn(Point(2,96))
	order = Column(Integer)

	def __repr__(self):
		return "<Raster('%s','%s')>" % (self.name, self.url)

class Location(Base):
	__tablename__ = 'app_location'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	description = Column(String)
	favorite = Column(Boolean)
	date = Column(Date)
	point = GeometryColumn(Point(2,96))
	
	def __repr__(self):
		return "<Location('%s','%s')>" % (self.id, self.name)

class Workspace(Base):
	__tablename__ = 'app_workspace'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	description = Column(String)
	layers = Column(String)
	overlays = Column(String)
	baselayer = Column(String)
	public = Column(Boolean)
	user_name = Column(String)
	date = Column(Date)
	point = GeometryColumn(Point(3,96))
	users = relationship('User', secondary=user_workspaces, backref='app_workspace')
	
	def __repr__(self):
		return "<Workspace('%s','%s')>" % (self.id, self.name)

class Group(Base):
	__tablename__ = 'app_group'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	description = Column(String)
	
	def __repr__(self):
		return "<Group('%s','%s')>" % (self.id, self.name)

class Role(Base):
	__tablename__ = 'app_role'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	description = Column(String)
	
	def __repr__(self):
		return "<Role('%s','%s')>" % (self.id, self.name)
		

class File(Base):
	__tablename__ = 'app_file'
	id = Column(Integer, primary_key=True)
	file_physical_name = Column(String)
	file_name = Column(String)
	description = Column(String)
	date = Column(Date)

	def __repr__(self):
		return "<Role('%s','%s')>" % (self.id, self.file_name)