import json
from bottle import get

import phi.core.repository as repo
from phi.rest import rest_method, db_session
import phi.rest.vo as vo

@get('group/all')
@rest_method
def all():
	groups = repo.Group(db_session).all()
	o = map(lambda r: vo.group(r), groups)
	return vo.collection(o, len(o))