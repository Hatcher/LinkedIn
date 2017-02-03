import socket
import socks
import httplib

#Set the port used for tor
SOCKS_PORT = 9050

def startTor():

def connectTor():
	#We route traffic through tor in order to keep our ip from being blacklisted.
	
	'''
	Setup Socks5 sockets.
	Use the socks socket as the default socket for routing traffic.
	'''
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', SOCKS_PORT, True)
	socket.socket = socks.socksocket
	

