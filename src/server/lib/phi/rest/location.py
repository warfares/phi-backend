from bottle import *
from shapely.geometry import Point
from geoalchemy import WKTSpatialElement

import json

import phi.core.model as model
import phi.core.repository as repo
import phi.rest.vo as vo


import phi.core.session_helper as session_helper
session = session_helper.create_session()


#Collections 

@route('location/all')
def all():
	locations = repo.Location(session=session).all()
	o = map(lambda l: vo.location(l), locations)
	session.close()
	session.remove()
	return vo.collection(o, len(o))

#CRUD

@post('location')
def create():
	o = json.load(request.body)
	user_name = o['userName']
	name = o['name']
	description = o['description']
	point = o['point']
	favorite = o['favorite']
	
	l = model.Location()
	l.name = name
	l.description = description
	l.favorite = favorite
	l.point = WKTSpatialElement(Point(point['x'], point['y']).wkt,96)
	
	repo.Location(session=session).create(l)
	
	repo_user = repo.User(session=session)
	user = repo_user.read(user_name)
	user.locations.append(l)
	repo_user.update(user)
	session.close()
	session.remove()
	return vo.success(True)

@route('location/:id')
def read(id):
	l = repo.Location(session=session).read(id)
	o = vo.location(l) if l else ''
	session.close()
	session.remove()
	return o
	
@put('location')
def update():
	o = json.load(request.body)
	id = o['id']
	name = o['name']
	description = o['description']

	repo_location = repo.Location(session=session)
	l = repo_location.read(id)
	l.name = name
	l.description = description
	repo_location.update(l)
	session.close()
	session.remove()
	return vo.success(True)

@delete('location/:id')
def delete(id):
	repo_location = repo.Location(session=session)
	l = repo_location.read(id)
	repo_location.delete(l)
	session.close()
	session.remove()
	return vo.success(True)

@post('location/favorite')
def favorite():
	o = json.load(request.body)
	id = o['id']
	favorite = o['favorite']

	repo_location = repo.Location(session=session)
	l = repo_location.read(id)
	l.favorite = favorite
	repo_location.create(l)
	session.close()
	session.remove()
	return vo.success(True)