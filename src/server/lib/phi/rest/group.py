from bottle import *
import json
import phi.core.model as model
import phi.core.repository as repo

import phi.rest as module
import phi.rest.vo as vo

@route('group/all')
@module.rest_method
def all():
	groups = repo.Group(session = module.session).all()
	o = map(lambda r: vo.group(r), groups)
	return vo.collection(o, len(o))