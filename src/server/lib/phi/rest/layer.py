import json
from bottle import get, request

import phi.core.repository as repo
from phi.rest import rest_method, db_session
import phi.rest.vo as vo

@get('layer/all')
@rest_method
def all():
	layers = repo.Layer(db_session).all()
	o = map(lambda l: vo.layer(l), layers)
	return vo.collection(o, len(o))

@get('layer')
@rest_method
def read():
	layer_name = request.GET.get('layerName')
	l = repo.Layer(db_session).read(layer_name)
	o = vo.layer(l) if l else ''
	return o


#User Locations
@get('layer/getfiles')
@rest_method
def get_locations():
	layer_name = request.GET.get('layerName')
	start = int(request.GET.get('start'))
	limit = int(request.GET.get('limit'))

	files = repo.Layer(db_session).read(layer_name).files

	#paging by code (discrete values)
	total = len(files)
	limit = start + limit

	o = map(lambda f: vo.file(f), files[start:limit])
	return vo.collection(o, total)