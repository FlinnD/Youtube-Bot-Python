from apiclient.discovery import build
from apiclient.errors import Httperror
from oauth2client.tools import argparser



API_KEY = "xxxxxx"

API_NAME = "youtube"

API_VERSION = "v3"


def main(options):

conn = build(API_NAME, API_VERSION, developerKey = API_KEY)

channel = conn.channels().list(
	id = options.channelid,
	part = "snippet,statistics"
).execute()

title = channel["items"]["snippet"]["title"] 	
subs = channel["items"]["statistics"]["subscriberCount"] 		
videoNo = channel["items"]["statistics"]["videoCount"] 		
views = channel["items"]["statistics"]["viewCount"] 

print "/n title: {} /n Subscribers: {} /n Number of videos: {} /n Number of views: {}"


if __NAME__ == __MAIN__:
	
	argparser.add_argument("--channelid", help = "id of the specified channel")
	argparser.add_argument("--results", help = "number of channels before stopping", default = "25")
	options = argparser.parse_args()
	
	try:
		main(options)
	except HttpError e:
		print "HTTP Error {} occured:/n{}".format(e.resp.status,e.content)