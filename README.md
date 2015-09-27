Stupid script that I found useful to add a list of vlans from a file when doing a pentest of 90+ VLANs with 5 laptops. This utility only creates the interface, it does not configure them. 

'''
shell$ python massvlan.py 
USAGE:

This utility adds vlans from a list called vlans.txt

 Add vlans:
	massvlan.py -i eth0 -f vlans.txt -a

 Remove vlans:
	massvlan.py -i eth0 -f vlans.txt -d
	
	shell$
'''
