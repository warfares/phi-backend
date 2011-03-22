import json
from bottle import get

import phi.core.repository as repo
import phi.rest as module
import phi.rest.vo as vo

@get('group/all')
@module.rest_method
def all():
	groups = repo.Group(session = module.db_session).all()
	o = map(lambda r: vo.group(r), groups)
	return vo.collection(o, len(o))