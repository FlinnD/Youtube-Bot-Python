
class channelAnalytics:
	
	def __init__(self,chanId,conn):

		self.chanId = chanId
		self.conn = conn

		self.channel = self.conn.channels().list(
			id = self.chanId,
			part = "snippet,statistics,contentDetails"
		).execute()


	def getChanViews(self):
		views = ''
		for i in self.channel.get("items",[]):
			views = i["statistics"]["viewCount"]
			
		return views


	def getChanSubs(self):
		subs = ''
		for i in self.channel.get("items",[]):
			subs = i["statistics"]["subscriberCount"]
			
		return subs


	def getChanUploads(self):
		videoNo = ''
		for i in self.channel.get("items",[]):
			videoNo = i["statistics"]["videoCount"]
			
		return videoNo


	def getChanTitle(self):
		title = ''
		for i in self.channel.get("items",[]):
			title = i["snippet"]["viewCount"]
				
		return title


	def getChanPlaylistId(self):
		id = ''
		for i in self.channel.get("items",[]):
			id = i["contentDetails"]["relatedPlaylists"]["uploads"]
		
		return id	

