import logging
import phi.core.session_helper as session_helper
import random 
import sys

LOG_FILENAME = '/log/debug.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

session = session_helper.create_session()


def rest_method(f, *args, **kwargs):
	def wrapper(*args, **kwargs):
		
		rid = random.randint(0,10000)
		logging.debug('BEGIN rest async call:#' + str(rid) + ' ' + f.__name__)
		
		#TODO check AUTHENTICATED user
		
		r = f(*args, **kwargs)
		
		session.close()
		session.remove()
		logging.debug('END rest sync call:#' + str(rid) + ' ' + f.__name__)
		return r
	return wrapper