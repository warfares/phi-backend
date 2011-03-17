import logging
import phi.core.session_helper as session_helper
import random 
import sys

#init logger 
LOG_FILENAME = '/log/debug.log'
FORMAT = "%(levelname)s %(asctime)s %(message)s"
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG, format=FORMAT)
logger = logging.getLogger("restlog")

#init session
db_session = session_helper.create_session() 


def rest_method(f, *args, **kwargs):
	'''Common rest db actions decorator'''
	
	def wrapper(*args, **kwargs):
		
		#logger
		rid = random.randint(0,10000)
		logger.debug('BEGIN rest async call:#' + str(rid) + ' ' + f.__name__)
		
		#TODO check AUTHENTICATED (session) user
		
		r = f(*args, **kwargs)
		
		db_session.close()
		db_session.remove()
		logger.debug('END rest sync call:#' + str(rid) + ' ' + f.__name__)
		return r
	return wrapper