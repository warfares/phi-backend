import json
from bottle import get

import phi.core.repository as repo
import phi.rest as module
import phi.rest.vo as vo

@get('role/all')
@module.rest_method
def all():
	roles = repo.Role(session = module.db_session).all()
	o = map(lambda r: vo.role(r), roles)
	return vo.collection(o, len(o))