from bottle import *
import json
import phi.core.model as model
import phi.core.repository as repo
import phi.rest.vo as vo

import phi.core.session_helper as session_helper
session = session_helper.create_session()

@route('layer/all')
def all():
	layers = repo.Layer(session = session).all()
	o = map(lambda l: vo.layer(l), layers)
	session.close()
	session.remove()
	return vo.collection(o, len(o))

@route('layer/:id')
def read(id):
	l = repo.Layer(session = session).read(id)
	o = vo.layer(l) if l else ''
	session.close()
	session.remove()
	return o