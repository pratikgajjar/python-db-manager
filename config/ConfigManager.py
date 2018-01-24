from ConfigParser import ConfigParser,SafeConfigParser
import os.path
class ConfigManager():
	"""docstring for ConfigManager"""
	__file_path = ''
	def __init__(self):
		# print("ConfigManager obj created")
		_dir = os.path.dirname(os.path.abspath(__file__))
		self.__file_path = _dir + '/config.ini'

	def read_from_config(self,section):
		config = ConfigParser()
		try:
			with open(self.__file_path) as f:
				config.readfp(f)
				return dict(config._sections[section])
		except Exception as e:
				raise e
		return -1		
	
	def edit_config_file(self,section,dataDict):
		parser = SafeConfigParser()
		#ReadFile
		try:
			with open(self.__file_path) as f:
				parser.readfp(f)
		except Exception as e:
			raise e
		#Set new Data to obj parser
		for key in dataDict:	
			parser.set(section, key, dataDict[key])
		#Write content to file from obj parser
		try:
			with open(self.__file_path,'w') as f:
				parser.write(f)
				return 1	
		except Exception as e:
			raise e
		return -1	