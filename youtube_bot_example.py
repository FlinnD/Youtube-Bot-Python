from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from Analytics import *


API_KEY = "xxxxxxxxxxxx"

API_NAME = "youtube"

API_VERSION = "v3"


def main(options):
	conn = build(API_NAME, API_VERSION, developerKey = API_KEY)

	channel = channelAnalytics(options.channelid,conn)
	'''
	print(channel.getChanPlaylistId())
	
	chanVids = playlistAnalytics(channel.getChanPlaylistId(),conn,options.channelid)
	videoIds = chanVids.getVideoIds()
	videos = videoAnalytics(videoIds,conn,options.channelid)
	print(videos.getVidTitles())
	#do anything here e.g. send data to sql server
	'''
	if int(channel.getChanSubs()) < 100000:
		chanVids = playlistAnalytics(channel.getChanPlaylistId(),conn,options.channelid)

		videoIds = chanVids.getVideoIds()

		videos = videoAnalytics(videoIds,conn,options.channelid)

		#dict_Array = videos.getDictionaryArray()
		
		for x in videos.getVidViews():
			print("\nviews:{}\n").format(x)



if __name__ == '__main__':
	
	argparser.add_argument("--channelid", help = "id of the specified channel")
	#argparser.add_argument("--results", help = "number of channels before stopping", default = "25")
	options = argparser.parse_args()
	
	try:
		main(options)

	except HttpError as e:
		print "HTTP Error {} occured:\n{}".format(e.resp.status,e.content)