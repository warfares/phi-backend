from bottle import *
import json
import phi.core.model as model
import phi.core.repository as repo

import phi.rest as module
import phi.rest.vo as vo

@route('layer/all')
@module.rest_method
def all():
	layers = repo.Layer(session = module.db_session).all()
	o = map(lambda l: vo.layer(l), layers)
	return vo.collection(o, len(o))

@route('layer/:id')
@module.rest_method
def read(id):
	l = repo.Layer(session = module.db_session).read(id)
	o = vo.layer(l) if l else ''
	return o