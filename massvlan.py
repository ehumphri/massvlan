import os,sys,getopt
from subprocess import call
 
devnull = open(os.devnull, 'w')
script = os.path.basename(__file__)

def addvlan ( intf, vlan ):
  print "adding " + str(vlan).strip() 
  vintf = intf+"."+vlan.strip()
  call(["vconfig","add",intf,vlan],stdout=devnull)
  call(["ifconfig",vintf,"up"],stdout=devnull,stderr=devnull)

def delvlan ( intf, vlan ):
   print "removing " + str(vlan).strip()
   vintf = intf+"."+vlan.strip()
   call(["vconfig","rem",vintf],stdout=devnull,stderr=devnull)

def getvlans ( filename ):
  global vlanids

  if os.path.isfile(filename):
    with open(filename) as f:
      vlanids = f.readlines()
    f.close()
  else:
    print "\nERROR: File not found\n"
    usage()
    sys.exit(2)

def usage ():
  print "USAGE:"
  print "\nThis utility adds vlans from a list called vlans.txt\n"
  print " Add vlans:"
  print "\t"+script + ' -i eth0 -f vlans.txt -a'
  print "\n Remove vlans:"
  print "\t"+script + ' -i eth0 -f vlans.txt -d'
  print ""


def main(argv):

   if len(argv) == 0:
     usage()
     sys.exit(0)
  
   intf = 'eth0'       # default interface
   file = 'vlans.txt'  # default filename
   try:
      opts, args = getopt.getopt(argv,"hadi:f:",["interface","file","add","del"])
   except getopt.GetoptError:
      usage()
      sys.exit(2)
   for opt, arg in opts:

      if opt == '-h':
	 usage()
   	 sys.exit()

      elif opt in ("-i", "--interface"):
        intf = arg;
	print "Interface " + intf + " selected"

      elif opt in ("-f", "--file"):
     	file = arg	 

      elif opt in ("-a", "--add"):
	getvlans(file)
	print "Adding VLANs"
        for vlan in vlanids:
	  addvlan (intf,vlan)

      elif opt in ("-d", "--del"):
	getvlans(file)
	print "Deleting VLANs"
        for vlan in vlanids:
	  delvlan ( intf,vlan )

      else:
	usage()
  	sys.exit()

if __name__ == "__main__":
   main(sys.argv[1:])

