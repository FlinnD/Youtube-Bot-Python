
class videoAnalytics:

	def __init__(self,videoIds,conn,chanId):

		self.conn = conn
		self.videoIds = videoIds
		self.chanId = chanId
		videoViews = []
		videoTitles = []
		videoDesc = []


		vidString = ','.join(map(str, videoIds))

		vids = self.conn.videos().list(
			id = vidString,
			part = "snippet,statistics"
		).execute()

		for vid in vids.get('items',[]):
			videoViews.append(vid["statistics"]["viewCount"])
			videoTitles.append(vid["snippet"]["title"])
			videoDesc.append(vid["snippet"]["description"])

		view_Dict = dict(zip(videoIds,videoViews))
		title_Dict = dict(zip(videoIds,videoTitles))
		desc_Dict = dict(zip(videoIds,videoDesc))
		dict_Array = [view_Dict,title_Dict,desc_Dict]
		
		self.videoViews = videoViews
		self.videoTitles = videoTitles
		self.videoDesc = videoDesc
		self.view_Dict = view_Dict
		self.title_Dict = title_Dict
		self.desc_Dict = desc_Dict
		self.dict_Array = dict_Array

		'''

		for video in videoIds:


			vid = self.conn.videos().list(
				id = video,
				part = "snippet,statistics"
			).execute()

			videoViews.append(vid["items"]["statistics"]["viewCount"])
			videoTitles.append(vid["items"]["snippet"]["title"])

		vid_Dict = dict(zip(videoTitles,videoViews))

		'''

	def getVidViews(self):
		return self.videoViews

	def getVidTitles(self):
		return self.videoTitles

	def getVidDesc(self):
		return self.vidDesc	

	def getVideoDictionary(self):
		return self.vid_Dict

	def getDictionaryArray(self):
		return self.dict_Array


	def getChanId(self):
		return self.chanId



