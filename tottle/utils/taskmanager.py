import typing
import asyncio


class TaskManager:
	def __init__(self, loop: asyncio.AbstractEventLoop = None):
		self.loop: asyncio.AbstractEventLoop = loop or asyncio.get_event_loop()

		self.tasks: typing.List[typing.Callable] = []

	def run(self):
		[self.loop.create_task(task) for task in self.tasks]
		self.loop.run_forever()

	def close(self):
		self.loop.close()

	def add_task(self, task: typing.Union[typing.Coroutine, typing.Callable]):
		if asyncio.iscoroutinefunction(task):
			self.tasks.append(task())
		elif asyncio.iscoroutine(task):
			self.tasks.append(task)
		else:
			raise TypeError('Unknown task type!')
