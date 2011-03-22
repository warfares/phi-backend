import json
from bottle import get, post, put, delete, request
from shapely.geometry import Point
from geoalchemy import WKTSpatialElement

import phi.core.model as model
import phi.core.repository as repo
import phi.rest as module
import phi.rest.vo as vo


#Collections
@get('location/all')
@module.rest_method
def all():
	locations = repo.Location(session=module.db_session).all()
	o = map(lambda l: vo.location(l), locations)
	return vo.collection(o, len(o))

#CRUD
@post('location')
@module.rest_method
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
	
	repo.Location(session=module.db_session).create_update(l)
	
	repo_user = repo.User(session=module.db_session)
	user = repo_user.read(user_name)
	user.locations.append(l)
	repo_user.create_update(user)
	return vo.success(True)

@get('location/:id')
@module.rest_method
def read(id):
	l = repo.Location(session=module.db_session).read(id)
	o = vo.location(l) if l else ''
	return o
	
@put('location')
@module.rest_method
def update():
	o = json.load(request.body)
	id = o['id']
	name = o['name']
	description = o['description']

	repo_location = repo.Location(session=module.db_session)
	l = repo_location.read(id)
	l.name = name
	l.description = description
	repo_location.create_update(l)
	return vo.success(True)

@delete('location/:id')
@module.rest_method
def delete(id):
	repo_location = repo.Location(session=module.db_session)
	l = repo_location.read(id)
	repo_location.delete(l)
	return vo.success(True)

@post('location/favorite')
@module.rest_method
def favorite():
	o = json.load(request.body)
	id = o['id']
	favorite = o['favorite']

	repo_location = repo.Location(session=module.db_session)
	l = repo_location.read(id)
	l.favorite = favorite
	repo_location.create_update(l)
	return vo.success(True)