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