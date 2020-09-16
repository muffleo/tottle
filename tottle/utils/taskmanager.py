import asyncio
from typing import (
	Awaitable,
	Callable,
	Coroutine,
	List,
	Optional,
	Union,
)
from tottle.utils.logger import logger

CA = Union[Awaitable, Callable]


class TaskManager:
	def __init__(
			self,
			loop: Optional[asyncio.AbstractEventLoop] = None,
			*,
			on_startup: Optional[Callable] = None,
			on_shutdown: Optional[Callable] = None,
	):
		self.tasks: List[Callable] = []
		self.loop: asyncio.AbstractEventLoop = loop or asyncio.get_event_loop()

		self.on_shutdown: CA = on_shutdown
		self.on_startup: CA = on_startup

	def add_task(self, task: Union[Coroutine, Callable]):
		if asyncio.iscoroutinefunction(task):
			self.tasks.append(task())
		elif asyncio.iscoroutine(task):
			self.tasks.append(task)
		else:
			raise TypeError('Unknown task type!')

	def run(self):
		try:
			if self.on_startup is not None:
				self.loop.run_until_complete(self.on_startup())

			[self.loop.create_task(task) for task in self.tasks]
			self.loop.run_forever()

		except KeyboardInterrupt:
			logger.warning("Keyboard interrupt")
			self.close()

		finally:
			if self.on_shutdown is not None:
				self.loop.run_until_complete(self.on_shutdown())
			if not self.loop.is_running():
				self.close()

	def close(self):
		self.loop.close()
