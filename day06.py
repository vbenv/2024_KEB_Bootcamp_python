def desc(f):
	def wrapper():
		print("w")
		f()
	#print("a")
	return wrapper

# @desc
def something():
	print("do sth")

s = desc(something)
s()
#something()