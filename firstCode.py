import urllib
import re

print "we will try to get public IP address:"

url = "http://checkip.dyndns.org"
request = urllib.urlopen(url).read()
theIP = re.findall(r'[0-9]+(?:\.[0-9]+){3}', request)

print "And yes public IP is:", theIP
