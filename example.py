import os
from fitparse import FitFile

fitfile_path = os.path.join('data', '20140122-182824-1-1328-ANTFS-4-0.FIT')
fitfile = FitFile(fitfile_path)
fitfile.parse()


records = list(fitfile.get_messages())
for record in records:
	print "------------------------------------"
	print record
	for field in record:
		print (field.name, field.value, field.units)

