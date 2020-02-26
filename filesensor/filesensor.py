from .sources import localFileSysytem

class FileSensor:
	@classmethod
	def createObject(cls, path, sensor_type, update_frequency = 1):
		if sensor_type == 'local':
			return cls._get_local_object(cls(), path, update_frequency)
		else:
			return cls._get_local_object(cls(), path, update_frequency)

	
	def _get_local_object(self, path, update_frequency):
		return localFileSysytem.LocalFileSensor(path, update_frequency)
