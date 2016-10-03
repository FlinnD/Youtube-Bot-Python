from apiclient.discovery import build
#from apiclient.errors import HttpError
from oauth2client.tools import argparser



API_KEY = "xxxxxxxxxx"

API_NAME = "youtube"

API_VERSION = "v3"


def main(options):
	title = ''
	subs = ''
	videoNo = ''
	views = ''
	conn = build(API_NAME, API_VERSION, developerKey = API_KEY)

	channel = conn.channels().list(
		id = options.channelid,
		part = "snippet,statistics"
	).execute()
	for i in channel.get("items",[]):
		title = i["snippet"]["title"] 	
		subs = i["statistics"]["subscriberCount"] 		
		videoNo = i["statistics"]["videoCount"] 		
		views = i["statistics"]["viewCount"] 
	print("\n title: {} \n Subscribers: {} \n Number of videos: {} \n Number of views: {}").format(title,subs,videoNo,views)


if __name__ == '__main__':
	
	argparser.add_argument("--channelid", help = "id of the specified channel")
	#argparser.add_argument("--results", help = "number of channels before stopping", default = "25")
	options = argparser.parse_args()
		
	try:
		main(options)
	except HttpError as e:
		print "HTTP Error {} occured:/n{}".format(e.resp.status,e.content)