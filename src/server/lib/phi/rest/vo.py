''' vo -> objects python to JS notation '''
from shapely.wkb import loads 

#general purpose 
def collection(entities,total):
	vo = {
		'entities': entities,
		'total' : total
	}
	return vo

def entity(o):
	vo = {
		'id':o.id,
		'name':o.name,
		'description':o.description
	}
	return vo

def action(success,error=''):
	vo = {
		'success': success,
	    'errorMsg': error 
	}
	return vo

def auth(user,success, error=''):
	vo = {
		'user': user,
		'success': success,
	    'errorMsg': error
	}
	return vo

#geom vo def
def point(o):
	vo = { 
		'x': o.x, 
		'y': o.y 
	}
	if (o.has_z):
		vo['z'] = o.z
	return vo


#model entities.
#user
def user_base(o):
	vo = {
		'userName':o.user_name,
		'name':o.name,
		'lastName':o.last_name,
		'email':o.email
	}
	return vo

def user(o):
	vo = {
		'userName':o.user_name,
		'name':o.name,
		'lastName':o.last_name,
		'email':o.email,
		'roles': map(lambda r: entity(r), o.roles),
		'groups':map(lambda g: entity(g), o.groups)
	}
	return vo

#extjs node (layer) 
class ExtNode:
	def __init__(self, id, text):
		self.id = id
		self.text = text
		self.leaf = False
		self.expanded = False
		self.checked = False
		self.children = []
		self.layerId = ''
		self.srid = -1


def build_tree(ext_node, nodes):
	# take care with order.
	child_nodes_sort = sorted(filter(lambda n: n.parent_id == ext_node.id, nodes), key=lambda n: n.order)
	for t in child_nodes_sort:
		ext_child = ExtNode(t.id, t.description)
		if (t.leaf):
			ext_child.leaf = True
			ext_child.layerId = t.layer.name
			ext_child.srid = t.layer.srid
		ext_node.children.append(ext_child.__dict__)
		build_tree(ext_child, nodes)

#raster 
def raster(o):
	p = loads(str(o.point.geom_wkb))
	min = loads(str(o.min.geom_wkb))
	max = loads(str(o.max.geom_wkb))
	vo = {
		'id':o.id,
		'name':o.name,
		'description':o.description,
		'visible':o.visible,
		'url': o.url,
		'minz': o.minz,
		'maxz': o.maxz,
		'order': o.order,
		'point': point(p),
		'min': point(min),
		'max': point(max)
	}
	return vo

#layer	
def layer(o):
	vo = {
		'name':o.name,
		'project':o.project,
		'title':o.title,
		'type': o.type,
		'date': o.date.ctime(),
		'srid': o.srid
	}
	return vo

#location
def location(o):
	p = loads(str(o.point.geom_wkb))
	vo = {
		'id':o.id,
		'name':o.name,
		'description':o.description,
		'favorite':o.favorite,
		'date':o.date.ctime(),
		'point': point(p)
	}
	return vo

#workspace
def workspace(o):
	p = loads(str(o.point.geom_wkb))
	vo = {
		'id':o.id,
		'name':o.name,
		'description':o.description,
		'layers':o.layers,
		'overlays':o.overlays,
		'baselayer':o.baselayer,
		'public':o.public,
		'userName':o.user_name,
		'date':o.date.ctime(),
		'point': point(p)
	}
	return vo

#role
def role(o):
	vo = {
	'id':o.id,
	'name':o.name,
	'description':o.description
	}
	return vo

#group
def group(o):
	vo = {
	'id':o.id,
	'name':o.name,
	'description':o.description
	}
	return vo