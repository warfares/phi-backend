from bottle import *
import phi.core.repository as repo
import phi.rest.vo as vo

@route('layer/read/:id')
def read(id):
	l = repo.Layer().read(id)
	o = vo.layer(l) if l else ''
	return o