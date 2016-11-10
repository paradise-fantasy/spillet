import subprocess

while True:
	
	proc = subprocess.Popen("explorenfc-basic", stdout=subprocess.PIPE, shell=True)
	(rfid, error) = proc.communicate()
	print rfid
	rfid_array = rfid.split(":")
	UID  = [rfid_array[-2][-3:].strip(), rfid_array[-1].strip()]
	print UID

