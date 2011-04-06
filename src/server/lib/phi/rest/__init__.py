import logging
import phi.core.session_helper as session_helper
import random 
import sys
import bottle

#init logger 
LOG_FILENAME = '/log/debug.log'
FORMAT = "%(levelname)s %(asctime)s %(message)s"
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG, format=FORMAT)
logger = logging.getLogger("restlog")

#init db (sql_alchemmy) session - session per request 
db_session = session_helper.create_session() 


#root node name 
root_node_name = 'Minera los Pelambres'

def rest_method(f, *args, **kwargs):
	'''Common rest db actions decorator'''
	
	def wrapper(*args, **kwargs):
		
		#rest method logger
		rid = random.randint(0,10000)
		logger.debug('BEGIN rest async call:# %s %s' %(str(rid), f.__name__))
		
		#authentication
		env_session = bottle.request.environ.get('beaker.session')
		if 'user_name' in env_session:
			r = f(*args, **kwargs)
			auth = True
		else:
			r = {'auth': False}
			auth = False
		
		#remove db (sql_alchemmy) session - session per request
		db_session.close()
		db_session.remove()
		logger.debug('END rest sync call:# %s %s - auth: %s' %(str(rid), f.__name__, str(auth)))
		return r
	return wrapper