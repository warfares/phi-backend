import sys
from bottle import *
import json
import phi.core.repository as repo
import phi.rest as module
import phi.rest.vo as vo
import phi.rest.util as util

from util import encode_password

#Collections

#TODO Search Users direct from DB.
@route('user/search')
@module.rest_method
def search():
	
	user_name_pattern = request.GET.get('userNamePattern')
	user_name_position = request.GET.get('userNamePosition')
	name_pattern = request.GET.get('namePattern')
	name_position = request.GET.get('namePosition')
	last_name_pattern = request.GET.get('lastNamePattern')
	last_name_position = request.GET.get('lastNamePosition')
	group_id = int(request.GET.get('groupId'))
	role_id = int(request.GET.get('roleId'))
	
	start = int(request.GET.get('start'))
	limit = int(request.GET.get('limit'))
	
	repo_user = repo.User(session=module.db_session)
	
	user_name = util.like_filter(user_name_position, user_name_pattern)
	name  = util.like_filter(name_position, name_pattern)
	last_name  = util.like_filter(last_name_position, last_name_pattern)
	
	total = int(repo_user.search_count(user_name, name, last_name, group_id, role_id))
	users = repo_user.search(user_name, name, last_name, group_id, role_id, start, limit)

	o = map(lambda u: vo.user_base(u), users)
	return vo.collection(o, total)


@route('user/all')
@module.rest_method
def all():
	users = repo.User(session=module.db_session).all()
	o = map(lambda u: vo.user_base(u), users)
	return vo.collection(o, len(o))

#CRUD
@post('user')
@module.rest_method
def create():
	o = json.load(request.body)
	user_name = o['userName']
	name = o['name']
	last_name = o['lastName']
	email = o['email']
	
	u = model.User()
	u.user_name = user_name
	u.name = name
	u.last_name = last_name
	u.email = email
	
	repo.User(session=module.db_session).create_update(u)
	return vo.success(True)

@route('user/:id')
@module.rest_method
def read(id):
	u = repo.User(session=module.db_session).read(id)
	o = vo.user(u) if u else ''
	return o

@put('user')
@module.rest_method
def update():
	o = json.load(request.body)
	user_name = o['userName']
	name = o['name']
	last_name = o['lastName']
	email = o['email']

	repo_user = repo.User(session=module.db_session)
	u = repo_user.read(user_name)
	u.name = name
	u.last_name = last_name
	u.email = email
	
	repo_user.create_update(u)
	return vo.success(True)

@delete('user/:id')
@module.rest_method
def delete(id):
	repo_user = repo.User(session=module.db_session)
	u = repo_user.read(id)
	repo_user.delete(u)
	return vo.success(True)


#TODO LDAP access...
@post('user/login')
@module.rest_method
def login():
	o = json.load(request.body)
	user_name = o["userName"]
	password = o["password"]
	
	u = repo.User(session=module.db_session).read(user_name)
	
	if(not u):
		return vo.login_success(None,False,'user doesnt exist')
	
	if(u.password != encode_password(password)):
		return vo.login_success(None,False,'wrong password')

	return vo.login_success(vo.user_base(u),True)


@post('user/setpassword')
@module.rest_method
def setpassword():
	o = json.load(request.body)
	user_name = o["userName"]
	password = o["password"]
	repo_user = repo.User(session=module.db_session)
	u = repo_user.read(user_name)
	u.password = encode_password(password)
	repo_user.create_update(u)

	return vo.success(True)

#User Locations
@route('user/getlocations')
@module.rest_method
def get_locations():
	user_name = request.GET.get('userName')
	start = int(request.GET.get('start'))
	limit = int(request.GET.get('limit'))

	locations = repo.User(session=module.db_session).read(user_name).locations

	#paging by code (discrete values)
	total = len(locations)
	limit = start + limit

	o = map(lambda l: vo.location(l), locations[start:limit])
	return vo.collection(o, total)

@route('user/getfavlocations')
@module.rest_method
def get_favlocations():
	user_name = request.GET.get('userName')	
	locations = repo.User(session=module.db_session).read(user_name).locations
	locations = filter(lambda l: l.favorite, locations)
	o = map(lambda l: vo.location(l), locations)
	return vo.collection(o, len(o))

#User Workspace
@route('user/searchworkspace')
@module.rest_method
def search_workspace():
	user_name = request.GET.get('userName')
	start = int(request.GET.get('start'))
	limit = int(request.GET.get('limit'))
	name_pattern = request.GET.get('namePattern')
	name_position = request.GET.get('namePosition')
	user_pattern = request.GET.get('userPattern')
	user_position = request.GET.get('userPosition')
	
	workspaces = repo.User(session=module.db_session).read(user_name).workspaces
	
	#filter owner
	workspaces = util.collection_filter(user_position, user_pattern, 'user_name', workspaces)
	
	#filter name
	workspaces = util.collection_filter(name_position, name_pattern, 'name', workspaces)

	#sort
	workspaces = sorted(workspaces, key=lambda l: l.name)
	
	total = len(workspaces)
	limit = start + limit
	
	o = map(lambda ws: vo.workspace(ws), workspaces[start:limit])
	return vo.collection(o, total)

#User Layers
@route('user/getlayers')
@module.rest_method
def get_layer():
	user_name = request.GET.get('userName')
	nodes = repo.User(session=module.db_session).read(user_name).nodes
	layers = map(lambda n: n.layer,filter(lambda n: n.leaf, nodes))
	
	#sort
	layers = sorted(layers, key=lambda l: l.title)
	o = map(lambda l: vo.layer(l), layers)
	return vo.collection(o, len(o))
	

@route('user/searchlayers')
@module.rest_method
def search_layer():
	user_name = request.GET.get('userName')
	start = int(request.GET.get('start'))
	limit = int(request.GET.get('limit'))
	pattern = request.GET.get('pattern')
	position = request.GET.get('position')
	type = request.GET.get('type')

	nodes = repo.User(session=module.db_session).read(user_name).nodes
	layers = map(lambda n: n.layer,filter(lambda n: n.leaf, nodes))

	#filter type
	if(type != '%'):
		layers = filter(lambda l: l.type == type, layers)
	
	#filter title
	layers = util.collection_filter(position, pattern, 'title', layers)

	#sort
	layers = sorted(layers, key=lambda l: l.title)
	
	total = len(layers)
	limit = start + limit

	o = map(lambda l: vo.layer(l), layers[start:limit])
	return vo.collection(o, total)

#User Nodes
@route('user/getnodes')
@module.rest_method
def get_nodes():
	user_name = request.GET.get('userName')
	nodes = repo.User(session=module.db_session).read(user_name).nodes
	
	tree = vo.ExtNode(0,'Minera los Pelambres')
	vo.build_tree(tree, nodes)
	return tree.__dict__

#User Raster
@route('user/getrasters')
@module.rest_method
def get_rasters():
	user_name = request.GET.get('userName')
	rasters = repo.User(session=module.db_session).read(user_name).rasters
	rasters = sorted(rasters, key=lambda r:r.order)
	o = map(lambda r: vo.raster(r), rasters)
	return vo.collection(o, len(o))