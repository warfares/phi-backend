from bottle import route, run, post, request
import json
import phi.core.repository as repo

import phi.rest as module
import phi.rest.vo as vo


@route('workspace/get_by_owner')
@module.rest_method
def get_by_owner():
	workspaces = repo.Workspace(session=module.session).get_by_owner('ldapellipse')
	o = map(lambda ws: vo.workspace(ws), workspaces)
	return vo.collection(o, len(o))