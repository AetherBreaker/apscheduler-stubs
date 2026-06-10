# Standard library imports
from abc import ABCMeta, abstractmethod
from datetime import datetime

class BaseTrigger(metaclass=ABCMeta):
  __slots__ = ()
  @abstractmethod
  def get_next_fire_time(self, previous_fire_time: datetime | None, now: datetime) -> datetime | None: ...
  def _apply_jitter(self, next_fire_time: datetime, jitter: int | None, now: datetime) -> datetime: ...
