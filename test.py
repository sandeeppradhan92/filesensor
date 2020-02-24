from filesensor import FileSensor, default_actions, exec, create_task


def create_async_tasks(path_list):	
	tasks = []
	for path in path_list:
		filesensor = FileSensor(path)
		filesensor.register_action_all(default_actions)
		task = create_task(filesensor)
		tasks.append(task)
	
	exec(tasks)

if __name__=='__main__':
	# Configuration Prameters

	# Provide the list of path that has to be watched
	path_list = ["/home/sandeep/code/github/filesensor/testFolder/f1", 
				 "/home/sandeep/code/github/filesensor/testFolder/f2"]
	
	create_async_tasks(path_list)
