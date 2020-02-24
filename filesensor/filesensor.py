import os
import asyncio
from operator import itemgetter
from functools import lru_cache

from .factory import ObjectFactory

class FileSensor(ObjectFactory):
	def __init__(self, path, update_frequency = 1):
		ObjectFactory.__init__(self)
		self.path = path
		self.update_frequency = update_frequency # In Seconds
		self.state=True
		self.file_map = {}
	
	@lru_cache(maxsize=256)
	def get_file_map(self, item_list, metadata):
		metadata = list(map(lambda x: x[1], metadata))
		return zip(metadata, item_list)

	def get_metadata(self, path):
		item_list = tuple(os.listdir(path))
		item_details = tuple(map(lambda item : tuple(os.stat(os.path.join(path, item))), item_list))
		self.file_map = self.get_file_map(item_list, item_details)
		item_details = sorted(item_details, key=itemgetter(8),reverse=True)
		return item_details


	async def watch(self):
		initial_details = self.get_metadata(self.path)
		initial_max_changed_ts = self.get_metadata(self.path)[0][8] if len(initial_details) else 0

		while self.state:
			updated_details = self.get_metadata(self.path)
			if len(updated_details):
				updated_max_changed_ts = updated_details[0][8]
				if (updated_max_changed_ts > initial_max_changed_ts):
					for details in updated_details:
						if(details[8] > initial_max_changed_ts):
							print("debugger")
							for key, value in self._actions.items():
								print(f"executing action : {key}")
								value.run(self.path, self.file_map, details)
					initial_max_changed_ts=updated_max_changed_ts
				await asyncio.sleep(self.update_frequency)

 