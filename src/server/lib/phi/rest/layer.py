import json
from bottle import get

import phi.core.repository as repo
from phi.rest import rest_method, db_session
import phi.rest.vo as vo

@get('layer/all')
@rest_method
def all():
	layers = repo.Layer(db_session).all()
	o = map(lambda l: vo.layer(l), layers)
	return vo.collection(o, len(o))

@get('layer/:id')
@rest_method
def read(id):
	l = repo.Layer(db_session).read(id)
	o = vo.layer(l) if l else ''
	return o