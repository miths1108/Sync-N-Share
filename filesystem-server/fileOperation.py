import os

def read(request):
	
	filename = "/home/sweksha/node_modules/share/examples/filesystem/"+request
	try:
		fp = open(filename, 'r')
		string = ''
		for line in fp:
			string = string + line
		fp.close()
	except:
		string = "null"
	print string	
	return string

def write(request):
	request = request.split('#')
	filename = "/home/sweksha/node_modules/share/examples/filesystem/"+request[0]
	content = '#'.join(request[1:])
	print content
	fp = open(filename,'w')
	fp.write(content)
	fp.close()
	return "done"

def rename(request):
	request = request.split('#')
	fileold = request[0]
	filenew = request[1]
	repoid = request[2]
	print fileold
	print filenew
	print repoid
	for filename in os.listdir("/home/sweksha/node_modules/share/examples/filesystem/"):
		if filename.startswith(repoid+'^'+fileold+'^'):
			version = filename[-1]
			print filename
			os.rename("/home/sweksha/node_modules/share/examples/filesystem/"+filename,"/home/sweksha/node_modules/share/examples/filesystem/"+repoid+'^'+filenew+'^'+version)
	return "done"