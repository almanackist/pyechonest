from pyechonest import artist
from pyechonest import config
config.ECHO_NEST_API_KEY="UVQRN626N0JKLRPDL"



def similar_artists(name):
	bk = artist.Artist(name)
	for similar_artist in bk.similar:
		print "\t%s" % (similar_artist.name,)
