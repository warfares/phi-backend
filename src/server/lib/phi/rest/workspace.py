from datetime import date

from bottle import *
import json
from shapely.geometry import Point
from geoalchemy import WKTSpatialElement

import phi.core.model as model
import phi.core.repository as repo
import phi.rest as module
import phi.rest.vo as vo


@route('workspace/get_by_owner')
@module.rest_method
def get_by_owner():
	user_name = request.GET.get('userName')
	start = int(request.GET.get('start'))
	limit = int(request.GET.get('limit'))
	
	workspaces = repo.Workspace(session=module.session).get_by_owner(user_name)
	#paging by code (discrete values)
	total = len(workspaces)
	limit = start + limit
	
	o = map(lambda ws: vo.workspace(ws), workspaces[start:limit])
	return vo.collection(o, total)


#CRUD
@post('workspace')
@module.rest_method
def create():
	o = json.load(request.body)
	user_name = o['userName']
	name = o['name']
	description = o['description']
	layers = o['layers']
	point = o['point']
	overlays = o['overlays']
	baselayer = o['baselayer']
	user_name = o['userName']

	ws = model.Workspace()
	ws.name = name
	ws.description = description
	ws.layers = layers
	ws.overlays = overlays
	ws.baselayer = baselayer
	ws.user_name = user_name
	ws.point = WKTSpatialElement(Point(point['x'], point['y']).wkt,96)
	ws.public = True
	ws.date = date.today()
	
	repo.Workspace(session=module.session).create_update(ws)

	repo_user = repo.User(session=module.session)
	user = repo_user.read(user_name)
	user.workspaces.append(ws)
	repo_user.create_update(user)
	return vo.success(True)

@route('workspace/:id')
@module.rest_method
def read(id):
	ws = repo.Workspace(session=module.session).read(id)
	o = vo.workspace(ws) if ws else ''
	return o

@put('workspace')
@module.rest_method
def update():
	o = json.load(request.body)
	id = o['id']
	name = o['name']
	description = o['description']
	layers = o['layers']
	point = o['point']
	overlays = o['overlays']
	baselayer = o['baselayer']

	repo_ws = repo.Workspace(session=module.session)
	ws = repo_ws.read(id)
	
	ws.name = name
	ws.description = description
	ws.layers = layers
	ws.overlays = overlays
	ws.baselayer = baselayer
	ws.point = WKTSpatialElement(Point(point['x'], point['y']).wkt,96)
	ws.public = True
	ws.date = date.today()
	
	repo_ws.create_update(ws)
	return vo.success(True)

@delete('workspace/:id')
@module.rest_method
def delete(id):
	repo_ws= repo.Workspace(session=module.session)
	ws = repo_ws.read(id)
	repo_ws.delete(ws)
	return vo.success(True)