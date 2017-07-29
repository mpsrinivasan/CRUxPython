import urllib;
import requests;

def noYTD():
	url = input("Enter URL: ");
	r = urllib.request.urlopen(url);
	url = url.split('/');
	bin_file = open(url[-1], 'wb');
	bin_file.write(r.read());
	bin_file.close();

def yesYTD():
	url = input("Enter URL: ");
	r = urllib.request.urlopen(url);
	url = url.split('/');
	name = list(url[-1]);
	name = name[8:-1];
	name = ''.join(name);
	print (name);
	name = name + '.mp4';
	#bin_file = open(name, 'wb');
	#bin_file.write(r.read());
	#bin_file.close();
isYTD = input("YouTube video?? ");

if (isYTD == 'n'):
	noYTD();
else:
	yesYTD();
