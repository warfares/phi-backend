#!/usr/bin/env python
# encoding: utf-8
from hashlib import sha256
import base64
import hmac

SALT = '+GNH}y<.vbgdayruTs1GXN2SK)/&%,$keu@jrsgnf:bDGSncfth4ayruykdHMnF' \
'=FZmx|ta;[Philosophy]yH9hiDA(./&/*ga~hyru5SytrhgD&(/IUlñ[' \
'JHGYUKTR~JbD#($CV7mMu-BNMJ¿mcvER{WER&%/(¨sFG!¡#?HE¡RUy>'


def encode_password(passw):
	'''SHA 256 base 64 encoded password'''
	hash = hmac.new(SALT,passw, sha256).digest()
	encoded = base64.b64encode(hash)
	return encoded
	
def collection_filter(position, pattern, attribute, collection):
	if(position == '0' and pattern != '' ):
		collection = filter(lambda o: getattr(o, attribute).find(pattern) != -1, collection) 
	if(position == '1'):
		collection = filter(lambda o: getattr(o, attribute).startswith(pattern), collection)
	if(position == '2'):
		collection = filter(lambda o: getattr(o, attribute).endswith(pattern), collection)
	if(position == '3'):
		collection = filter(lambda o: getattr(o, attribute).title == pattern, collection)
	
	return collection 
