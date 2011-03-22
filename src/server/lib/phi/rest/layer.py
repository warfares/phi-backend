from bottle import get
import json

import phi.core.repository as repo
import phi.rest as module
import phi.rest.vo as vo

@get('layer/all')
@module.rest_method
def all():
	layers = repo.Layer(session = module.db_session).all()
	o = map(lambda l: vo.layer(l), layers)
	return vo.collection(o, len(o))

@get('layer/:id')
@module.rest_method
def read(id):
	l = repo.Layer(session = module.db_session).read(id)
	o = vo.layer(l) if l else ''
	return o