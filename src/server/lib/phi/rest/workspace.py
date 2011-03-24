from datetime import datetime
import json

from bottle import get, post, put, delete, request

from shapely.geometry import Point
from geoalchemy import WKTSpatialElement

import phi.core.model as model
import phi.core.repository as repo

from phi.rest import rest_method, db_session
import phi.rest.vo as vo


@get('workspace/getbyowner')
@rest_method
def get_by_owner():
	user_name = request.GET.get('userName')
	start = int(request.GET.get('start'))
	limit = int(request.GET.get('limit'))
	
	workspaces = repo.Workspace(db_session).get_by_owner(user_name)
	#paging by code (discrete values)
	total = len(workspaces)
	limit = start + limit
	
	#order by date
	sort_ws = sorted(workspaces, key=lambda n: n.date, reverse=True)
	
	o = map(lambda ws: vo.workspace(ws), sort_ws[start:limit])
	return vo.collection(o, total)

#CRUD
@post('workspace')
@rest_method
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
	ws.date = datetime.now()
	
	repo.Workspace(db_session).create_update(ws)

	repo_user = repo.User(db_session)
	user = repo_user.read(user_name)
	user.workspaces.append(ws)
	repo_user.create_update(user)
	return vo.success(True)

@get('workspace/:id')
@rest_method
def read(id):
	ws = repo.Workspace(db_session).read(id)
	o = vo.workspace(ws) if ws else ''
	return o

@put('workspace')
@rest_method
def update():
	o = json.load(request.body)
	id = o['id']
	name = o['name']
	description = o['description']
	layers = o['layers']
	point = o['point']
	overlays = o['overlays']
	baselayer = o['baselayer']

	repo_ws = repo.Workspace(db_session)
	ws = repo_ws.read(id)
	
	ws.name = name
	ws.description = description
	ws.layers = layers
	ws.overlays = overlays
	ws.baselayer = baselayer
	ws.point = WKTSpatialElement(Point(point['x'], point['y']).wkt,96)
	ws.public = True
	ws.date = datetime.now()
	
	repo_ws.create_update(ws)
	return vo.success(True)

@delete('workspace/:id')
@rest_method
def delete(id):
	repo_ws= repo.Workspace(db_session)
	ws = repo_ws.read(id)
	repo_ws.delete(ws)
	return vo.success(True)


@get('workspace/getusers')
@rest_method
def get_users():
	id = int(request.GET.get('id'))
	start = int(request.GET.get('start'))
	limit = int(request.GET.get('limit'))

	workspace = repo.Workspace(db_session).read(id)
	users = workspace.users
	
	#paging by code (discrete values)
	total = len(users)
	limit = start + limit

	o = map(lambda u: vo.user(u), users[start:limit])
	return vo.collection(o, total)
	

@post('workspace/addusers')
@rest_method
def add_users():
	o = json.load(request.body)
	id = o["id"]
	user_names = o["userNames"]

	repo_workspace = repo.Workspace(db_session)
	repo_user = repo.User(db_session)

	workspace = repo_workspace.read(id)

	def add(user_name):
		u = repo_user.read(user_name)
		workspace.users.append(u)
		return True

	map(lambda user_name: add(user_name), user_names)
	
	repo_workspace.create_update(workspace)
	return vo.success(True)

@post('workspace/removeusers')
@rest_method
def remove_users():
	o = json.load(request.body)
	id = o["id"]
	user_names = o["userNames"]

	repo_workspace = repo.Workspace(db_session)
	repo_user = repo.User(db_session)

	workspace = repo_workspace.read(id)

	def remove(user_name):
		u = repo_user.read(user_name)
		if(u in workspace.users):
			workspace.users.remove(u)
		return True

	map(lambda user_name: remove(user_name), user_names)

	repo_workspace.create_update(workspace)
	return vo.success(True)