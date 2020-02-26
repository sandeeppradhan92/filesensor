import os
from operator import itemgetter

from ..filesensorFactory import FileSensorFactory

class LocalFileSensor(FileSensorFactory):
	def __init__(self, path, update_frequency = 1):
		FileSensorFactory.__init__(self, path, update_frequency)

	def get_metadata(self, path):
		item_list = tuple(os.listdir(path))
		item_details = tuple(map(lambda item : tuple(os.stat(os.path.join(path, item))), item_list))
		self.file_map = self._get_file_map(item_list, item_details)
		item_details = sorted(item_details, key=itemgetter(8),reverse=True)
		return item_details
