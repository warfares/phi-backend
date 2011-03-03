import sys
from bottle import *
import json
import phi.core.repository as repo
import phi.rest as module
import phi.rest.vo as vo


#Collections
@route('user/all')
@module.rest_method
def all():
	users = repo.User(session=module.session).all()
	o = map(lambda u: vo.user_base(u), users)
	return vo.collection(o, len(o))

#CRUD
@post('user')
@module.rest_method
def create():
	o = json.load(request.body)
	user_name = o['userName']
	name = o['name']
	#TODO all properties
	
	u = model.User()
	u.user_name = user_name
	u.name = name
	#TODO all properties
	
	repo.User(session=module.session).create_update(u)
	return vo.success(True)

@route('user/:id')
@module.rest_method
def read(id):
	u = repo.User(session=module.session).read(id)
	o = vo.user(u) if u else ''
	return o

@put('user')
@module.rest_method
def update():
	o = json.load(request.body)
	user_name = o['user_name']
	name = o['name']
	#TODO all properties

	repo_user = repo.User(session=module.session)
	u = repo_user.read(user_name)
	u.name = name
	#TODO all properties
	
	repo_user.create_update(u)
	return vo.success(True)

@delete('user/:id')
@module.rest_method
def delete(id):
	repo_user = repo.User(session=module.session)
	u = repo_user.read(id)
	repo_user.delete(u)
	return vo.success(True)


#TODO LDAP access... password auth ...
@post('user/login')
@module.rest_method
def login():
	o = json.load(request.body)
	user_name = o["user_name"]
	password = o["password"]
	u = repo.User(session=module.session).read(user_name)
	#TODO check password
	return {'user':vo.user_base(u), 'status':True} if u else {'user':user_name, 'status':False}


#TODO: fix paggin
@route('user/getlocations')
@module.rest_method
def get_locations():
	user_name = request.GET.get('userName')
	start = int(request.GET.get('start'))
	limit = int(request.GET.get('limit'))

	locations = repo.User(session=module.session).read(user_name).locations
	total = len(locations)

	#paging by code (discrete values)
	if (total - start < limit):
		limit = (total - start)

	locations = repo.User(session=module.session).read(user_name).locations[start:limit]
	o = map(lambda l: vo.location(l), locations)
	return vo.collection(o, total)

@route('user/getfavlocations')
@module.rest_method
def get_favlocations():
	user_name = request.GET.get('userName')	
	locations = repo.User(session=module.session).read(user_name).locations
	locations = filter(lambda l: l.favorite, locations)
	o = map(lambda l: vo.location(l), locations)
	return vo.collection(o, len(o))


#Layers
@route('user/getlayers')
@module.rest_method
def get_layer():
	user_name = request.GET.get('userName')
	nodes = repo.User(session=module.session).read(user_name).nodes
	layers = map(lambda n: n.layer,filter(lambda n: n.leaf, nodes))
	
	#sort
	layers = sorted(layers, key=lambda l: l.title)
	o = map(lambda l: vo.layer(l), layers)
	return vo.collection(o, len(o))
	

#search by code !!
@route('user/searchlayers')
@module.rest_method
def search_layer():
	user_name = request.GET.get('userName')
	start = int(request.GET.get('start'))
	limit = int(request.GET.get('limit'))
	pattern = request.GET.get('pattern')
	position = request.GET.get('position')
	type = request.GET.get('type')

	nodes = repo.User(session=module.session).read(user_name).nodes
	layers = map(lambda n: n.layer,filter(lambda n: n.leaf, nodes))

	#filter type
	if(type != '%'):
		layers = filter(lambda l: l.type == type, layers)
	
	#filter title
	if(position == '0' and pattern != '' ):
		layers = filter(lambda l: l.title.find(pattern) != -1, layers) 
	if(position == '1'):
		layers = filter(lambda l: l.title.startswith(pattern), layers)
	if(position == '2'):
		layers = filter(lambda l: l.title.endswith(pattern), layers)
	if(position == '3'):
		layers = filter(lambda l: l.title == pattern, layers)

	#sort
	layers = sorted(layers, key=lambda l: l.title)
	
	total = len(layers)
	limit = start + limit

	o = map(lambda l: vo.layer(l), layers[start:limit])
	module.session.close()
	module.session.remove()
	return vo.collection(o, total)

@route('user/getnodes')
@module.rest_method
def get_nodes():
	user_name = request.GET.get('userName')
	nodes = repo.User(session=module.session).read(user_name).nodes
	
	tree = vo.ExtNode(0,'Minera los Pelambres')
	vo.build_tree(tree, nodes)
	return tree.__dict__

@route('user/getrasters')
@module.rest_method
def get_rasters():
	user_name = request.GET.get('userName')
	rasters = repo.User(session=module.session).read(user_name).rasters
	rasters = sorted(rasters, key=lambda r:r.order)
	o = map(lambda r: vo.raster(r), rasters)
	return vo.collection(o, len(o))