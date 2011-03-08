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
	#filter const
	CONTAIN, START, END, EQUAL = '0','1','2','3'
		
	f = dict()
	f[CONTAIN] = lambda o: getattr(o, attribute).find(pattern) != -1
	f[START] = lambda o: getattr(o, attribute).startswith(pattern)
	f[END] = lambda o: getattr(o, attribute).endswith(pattern)
	f[EQUAL] = lambda o: getattr(o, attribute).title == pattern

	return filter(f[position], collection)
