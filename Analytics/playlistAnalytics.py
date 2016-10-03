
class playlistAnalytics:

	def __init__(self,playlistId,conn,chanId):
		videoIds = []
		self.playlistId = playlistId
		self.conn = conn
		self.chanId = chanId

		playlist = self.conn.playlistItems().list(
			playlistId = self.playlistId,
			maxResults = "50", #need to add user specified Result no.
			part = "contentDetails"
		).execute()
		for result in playlist.get("items",[]):
			videoIds.append(result["contentDetails"]["videoId"])
			
		self.videoIds = videoIds
	def getVideoIds(self):
	

		return self.videoIds	

	def getChanId(self):
	
		return self.chanId	
