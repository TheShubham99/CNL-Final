import socket

URL = raw_input("enter the url: ")
ip= socket.gethostbyname(URL)
print(ip)

ip=raw_input("enter ip: ")
URL=socket.gethostbyaddr(ip)
print(URL)


'''
Python Class: "socket" — Low-level networking interface

	This module provides access to the BSD socket interface.
	The socket() function returns a socket object whose methods implement the various socket system calls.

	Note: Some behavior may be platform dependent, since calls are made to the operating system socket APIs.




Functions used in above program:
	---socket.gethostbyname()
	---socket.gethostbyaddr()
	---InteractiveConsole.raw_input()
	---print()


---socket.gethostbyname(hostname)

	Translate a host name to IPv4 address format.
	The IPv4 address is returned as a string, such as '100.50.200.5'.
	If the host name is an IPv4 address itself it is returned unchanged.
	gethostbyname() does not support IPv6 name resolution.
	getaddrinfo() should be used instead for IPv4/v6 dual stack support.


---socket.gethostbyaddr(ip_address)

	Returns a triple (hostname, aliaslist, ipaddrlist)
	where: 	hostname is the primary host name responding to the given ip_address,
		aliaslist is a (possibly empty) list of alternative host names for the same address
		ipaddrlist is a list of IPv4/v6 addresses for the same interface on the same host.

	gethostbyaddr() supports both IPv4 and IPv6.


---InteractiveConsole.raw_input(prompt="")

	Write a prompt and read a line.
	The returned line does not include the trailing newline.
	When the user enters the EOF key sequence, EOFError is raised.
	The base implementation reads from sys.stdin.


---print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

	Print objects to the text stream file, separated by sep and followed by end.

	The file argument must be an object with a write(string) method;
	if it is not present or None, sys.stdout will be used.
	Since printed arguments are converted to text strings, print() cannot be used with binary mode file objects.
	For these, use file.write() instead.

	Whether output is buffered is usually determined by file.
	If the flush keyword argument is true, the stream is forcibly flushed.
'''
