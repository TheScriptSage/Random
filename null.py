class Null(object):
	def __init__(self, *args, **kwargs):
		self.args = args
		self.kwargs = kwargs
	def __call__(self, *args, **kwargs):
		print "Called: {0}, {1}".format(args, kwargs)
	def __str__(self):
		return "Null"
	def __int__(self):
		return 1
	def __dict__(self):
		return { "args": args, "kwargs": kwargs }
	def __list__(self):
		return [args, kwargs]
	def __getattr__(self, attr, *args, **kwargs):
		print "Attr called: {0}".format(attr)
		return Null(*args, **kwargs)

