
from geopy import geocoders
import csv

g = geocoders.GoogleV3()

def main():
	print("hello!")

	bars = []

	f = open("tabc latlng output.csv","r+")

	""" tabc houston addy could look something like:
	12423,"10739 NORTH FWY               ","HOUSTON             ",TX,77037
	12426,"23501 CINCO RANCH BLVD        ","HOUSTON             ",TX,77494
	12430,"24445 KATY FWY STE 500        ","HOUSTON             ",TX,77494
	12432,"4500 WASHINGTON AVE STE 200   ","HOUSTON             ",TX,77007
	12435,"12611 WOODFOREST BLVD STE F   ","HOUSTON             ",TX,77015
	12439,"16506 FM 529 RD               ","HOUSTON             ",TX,77095
	12440,"11130 BEECHNUT ST # A-C       ","HOUSTON             ",TX,77072
	12446,"15301 GULF FWY                ","HOUSTON             ",TX,77034
	"""

	with open('tabc houston addy.csv', 'rb') as csvfile:
		tabcreader = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in tabcreader:
			b = bar(row[0],row[1],row[2],row[3],row[4])
			try:
				b.makeLatLng()
			except Exception, e:
				print("couldn't get lat lng for " + b.id + " ,try again later.")
			
			bars.append(b)
			print "added bar " + b.id

	for bb in bars:
		if (bb.lat != ""):
			f.write(str(bb.dump()) + '\n')



class bar():
	lat = ""
	lng = ""

	def __init__(self,id,address,city,state,zip):
		self.id = id
		self.address = address
		self.city = city
		self.state = state
		self.zip = zip

	def makeLatLng(self):
		place, (lat, lng) = g.geocode(self.getaddy()) 
		self.lat = lat
		self.lng = lng 

	def getaddy(self):
		return self.address + " " + self.city  + " " + self.state  + " " + self.zip

	def dump(self):
		return self.id + "," + str(self.lat) + "," + str(self.lng)



if __name__ == "__main__": main()    

