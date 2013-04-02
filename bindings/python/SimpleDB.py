# this file has been automatically generated by valabind
from ctypes import *
from ctypes.util import find_library
lib = CDLL (find_library ('sdb'))
def instance (x):
	try:
		y = x.contents
		y.__init_methods__(y)
	except:
		pass
	return x
def register (self, name, cname, args, ret):
	g = globals ()
	g['self'] = self
	if (ret and ret!='' and ret[0]>='A' and ret[0]<='Z'):
		last = '.contents'
		ret2 = ' '
		ret = "instance(POINTER("+ret+"))"
	else:
		last = '.value'
		ret2 = ret
	setattr (self, cname, getattr (lib, cname))
	exec ('self.%s.argtypes = [%s]'%(cname, args))
	if ret != '':
		argstr = '' # object self.. what about static (TODO)
		for i in range (1, len(args.split (','))):
			argstr += ',' if i>1 else ' '
			argstr += 'x'+str(i)
		exec ('self.%s.restype = %s'%(cname, ret), g)
		argstr2 = '' # object self.. what about static (TODO)
		if argstr != '':
			argstr2 = ','+argstr
		exec ('self.%s = lambda%s: %s(self.%s(self._o%s))%s'%
			(name, argstr, ret2, cname, argstr2, last), g)
class SignalSource(Structure):
	_fields_ = [
	]
	def __init__(self, signum):
		Structure.__init__(self)
		g_unix_signal_source_new = lib.g_unix_signal_source_new
		g_unix_signal_source_new.restype = c_void_p
		self._o = g_unix_signal_source_new (signum)
		self.__init_methods__()
	def __init_methods__(self):
		if not hasattr(self,'_o'):
			self._o = addressof(self)
class Sdb(Structure):
	_fields_ = [
	]
	def __init__(self, name, locked):
		Structure.__init__(self)
		sdb_new = lib.sdb_new
		sdb_new.restype = c_void_p
		self._o = sdb_new (name, locked)
		self.__init_methods__()
	def __init_methods__(self):
		if not hasattr(self,'_o'):
			self._o = addressof(self)
		register(self,'sync','sdb_sync','c_void_p','c_bool')
		register(self,'query','sdb_query','c_void_p, c_char_p','c_bool')
		register(self,'querys','sdb_querys','c_void_p, c_char_p, c_int, c_char_p','c_char_p')
		register(self,'get','sdb_get','c_void_p, c_char_p, POINTER(c_int)','c_char_p')
		register(self,'add','sdb_add','c_void_p, c_char_p, c_char_p, c_uint','c_bool')
		register(self,'set','sdb_set','c_void_p, c_char_p, c_char_p, c_uint','c_bool')
		register(self,'alength','sdb_alength','c_void_p, c_char_p','c_int')
		register(self,'aget','sdb_aget','c_void_p, c_char_p, c_int, POINTER(c_uint)','c_char_p')
		register(self,'aset','sdb_aset','c_void_p, c_char_p, c_int, c_char_p, POINTER(c_uint)','c_char_p')
		register(self,'adel','sdb_adel','c_void_p, c_char_p, c_int, c_uint','c_bool')
		register(self,'setn','sdb_setn','c_void_p, c_char_p, c_ulonglong, c_uint','c_bool')
		register(self,'getn','sdb_getn','c_void_p, c_char_p, POINTER(c_uint)','c_ulonglong')
		register(self,'inc','sdb_inc','c_void_p, c_char_p, c_ulonglong, c_uint','c_ulonglong')
		register(self,'dec','sdb_dec','c_void_p, c_char_p, c_ulonglong, c_uint','c_ulonglong')
		register(self,'json_get','sdb_json_get','c_void_p, c_char_p, c_char_p, POINTER(c_uint)','c_char_p')
		register(self,'json_set','sdb_json_set','c_void_p, c_char_p, c_char_p, c_char_p, c_uint','c_char_p')
		register(self,'json_inc','sdb_json_inc','c_void_p, c_char_p, c_char_p, c_int, c_uint','c_int')
		register(self,'json_dec','sdb_json_dec','c_void_p, c_char_p, c_char_p, c_int, c_uint','c_int')
		register(self,'json_indent','sdb_json_indent','c_char_p','c_char_p')
		register(self,'json_unindent','sdb_json_unindent','c_char_p','c_char_p')
		register(self,'exists','sdb_exists','c_void_p, c_char_p','c_bool')
		register(self,'nexists','sdb_nexists','c_void_p, c_char_p','c_bool')
		register(self,'remove','sdb_remove','c_void_p, c_char_p, c_int','c_bool')
		register(self,'flush','sdb_flush','c_void_p',None)
		register(self,'get_expire','sdb_get_expire','c_void_p, c_char_p','c_ulonglong')
		register(self,'expire','sdb_expire','c_void_p, c_char_p, c_ulonglong','c_bool')
		register(self,'now','sdb_now','','c_ulonglong')
