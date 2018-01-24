from ..config.ConfigManager import ConfigManager
import MySQLdb

class DbManager():
	"""docstring for Db"""
	__mConfigManager = 0
	__db , __cursor = 0 , 0
	def __init__(self,dbSection):
		# print("DbManager obj created")
		self.__mConfigManager = ConfigManager()
		self.__db  = self.getDBconnection(dbSection)
		self.__cursor = self.__db.cursor(MySQLdb.cursors.DictCursor)
		
	def getDBconnection(self,dbSection):
		dbDict = self.__mConfigManager.read_from_config(dbSection)
		try:
			db = MySQLdb.connect(passwd=dbDict['passwd'], db=dbDict['db'], host=dbDict['host'], user=dbDict['user'], charset=dbDict['charset']) 	
		except Exception as e:
			print('Error : ' + str(e))
			raise e
		return db

	def executeQuery(self,query,qarg=""):
		try:
			if qarg == "":
				self.__cursor.execute(query)
			else:
				self.__cursor.execute(query,qarg)	
		except Exception as e:
			print('Error : ' + str(e))
			raise e
	
	def commitToDB(self):
		self.__db.commit()

	def fetchAllData(self):
		return self.__cursor.fetchall()
		
	def __del__(self):
		del self.__mConfigManager
		self.__db.close()