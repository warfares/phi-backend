import logging
import phi.core.session_helper as session_helper

LOG_FILENAME = '/log/example.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

session = session_helper.create_session()


def rest_method(f, *args, **kwargs):
	def wrapper(*args, **kwargs):
		logging.debug('rest call ')
		
		r = f(*args, **kwargs)
		
		session.close()
		session.remove()
		logging.debug('rest call end / session delete')
		return r
	return wrapper