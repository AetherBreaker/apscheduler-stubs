from _typeshed import Incomplete
from apscheduler.schedulers.blocking import BlockingScheduler

class BackgroundScheduler(BlockingScheduler):
  _thread: Incomplete
  _daemon: Incomplete
  def _configure(self, config) -> None: ...
  _event: Incomplete
  def start(self, *args, **kwargs) -> None: ...
  def shutdown(self, *args, **kwargs) -> None: ...
