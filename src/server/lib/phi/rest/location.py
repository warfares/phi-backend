from bottle import *
from shapely.geometry import Point
from geoalchemy import WKTSpatialElement

import json

import phi.core.model as model
import phi.core.repository as repo
import phi.rest.vo as vo

#Collections 

@route('location/all')
def all():
	locations = repo.Location().all()
	o = map(lambda l: vo.location(l), locations)
	
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
	
	repo.Location().create(l)
	
	repo_user = repo.User()
	user = repo_user.read(user_name)
	user.locations.append(l)
	repo_user.update(user)
	
	return vo.success(True)

@route('location/:id')
def read(id):
	l = repo.Location().read(id)
	o = vo.location(l) if l else ''
	
	return o
	
@put('location')
def update():
	o = json.load(request.body)
	id = o['id']
	name = o['name']
	description = o['description']

	repo_location = repo.Location()
	l = repo_location.read(id)
	repo_location.update(l)
	
	return vo.success(True)

@delete('location/:id')
def delete(id):
	repo_location = repo.Location()
	l = repo_location.read(id)
	repo_location.delete(l)
	
	return vo.success(True)

@post('location/favorite')
def enabled():
	o = json.load(request.body)
	id = o['id']
	favorite = o['favorite']

	repo_location = repo.Location()
	l = repo_location.read(id)
	l.favorite = favorite
	repo_location.update(l)
	
	return vo.success(True)