from bottle import *
from shapely.geometry import Point
from geoalchemy import WKTSpatialElement

import json

import phi.core.model as model
import phi.core.repository as repo
import phi.rest.vo as vo


@route('user/all')
def all():
	locations = repo.Location().all()
	o = map(lambda l: vo.location(l), locations)
	return vo.collection(o, len(o))

@route('location/:id')
def read(id):
	l = repo.Location().read(id)
	o = vo.location(l) if l else ''
	return o

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
	
	repoUser = repo.User()
	user = repoUser.read(user_name)
	user.locations.append(l)
	repoUser.update(user)
	
	return vo.ext_form(True)