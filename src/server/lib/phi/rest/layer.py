from bottle import *
import json
import phi.core.model as model
import phi.core.repository as repo
import phi.rest.vo as vo


@route('layer/all')
def all():
	layers = repo.Layer().all()
	o = map(lambda l: vo.layer(l), layers)
	return vo.collection(o, len(o))

@route('layer/:id')
def read(id):
	l = repo.Layer().read(id)
	o = vo.layer(l) if l else ''
	return o