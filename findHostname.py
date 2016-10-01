import socket
import sys
import uuid
    
def find(ipAddress):
	try:
		return socket.gethostbyaddr(ipAddress)[0]
	except socket.error:
		return None
		
def readFile(fileName):
	ipAddresses=[]
	try:
		with open(fileName) as fpIn:
			ipAddresses = fpIn.readlines()
	except:
		print "File not found!"
		sys.exit()
		
	return ipAddresses
	
def writeFile(result,outfilename):
	with open(outfilename, 'w') as fpOut:
		for item in result:
			print>>fpOut, item
	
def usage():
	print '''
		Usage:  findHostname.py ipAddresses.txt
	'''
	
def generateUniqueNumber():
	return uuid.uuid4().int & (1<<64)-1
	
	
result=[]
	
try:                 
	filename=sys.argv[1]
except IndexError:         
	usage()                         
	sys.exit(2)  
		
ipAddresses=readFile(filename)

if not ipAddresses:
	print "File is empty"
else:
	for ipAddress in ipAddresses:
		temp = ipAddress.strip()+" :"+str(find(ipAddress.strip()))
		print temp
		result.append(temp)

writeFile(result,"output_"+str(generateUniqueNumber())+".txt")
