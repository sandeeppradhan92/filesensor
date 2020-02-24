import asyncio

def exec(tasks):				 
	loop = asyncio.get_event_loop()
	loop.run_until_complete(asyncio.wait(tasks))  
	loop.close()

def create_task(filesensor):
	return asyncio.ensure_future(filesensor.watch())
