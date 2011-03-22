import json
from bottle import get

import phi.core.repository as repo

from phi.rest import rest_method, db_session
import phi.rest.vo as vo

@get('role/all')
@rest_method
def all():
	roles = repo.Role(db_session).all()
	o = map(lambda r: vo.role(r), roles)
	return vo.collection(o, len(o))