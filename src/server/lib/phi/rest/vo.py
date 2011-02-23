# vo-> objects python to JS notation 

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

#extjs node 
class ExtNode:
	def __init__(self, id, text):
		self.id = id
		self.text = text
		self.leaf = False
		self.expanded = False
		self.checked = False
		self.children = []
		self.layerId = ''


def build_tree(ext_node, nodes):
	# take care with order..
	for t in sorted(filter(lambda n: n.parent_id == ext_node.id, nodes), key=lambda n: n.order):
		ext_child = ExtNode(t.id, t.description)
		if (t.leaf):
			ext_child.leaf = True
			ext_child.layerId = t.layer.name
		ext_node.children.append(ext_child.__dict__)
		build_tree(ext_child, nodes)

#raster 
def raster(o):
	vo = {
		'id':o.id,
		'name':o.name,
		'description':o.description,
		'visible':o.visible,
		'url': o.url,
		'minz': o.minz,
		'maxz': o.maxz,
		'order': o.order
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
	vo = {
		'id':o.id,
		'name':o.name,
		'description':o.description,
		'favorite':o.favorite
	}
	return vo

#workspace
def workspace(o):
	vo = {
		'id':o.id,
		'name':o.name,
		'description':o.description,
		'layers':o.layers,
		'overlays':o.overlays,
		'baselayer':o.baselayer,
		'public':o.public,
		'userName':o.user_name,
		'date':o.date.ctime()
	}
	return vo