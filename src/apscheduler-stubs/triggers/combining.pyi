# Standard library imports
import abc
from datetime import datetime
from typing import TypedDict

# Third party imports
from apscheduler.triggers.base import BaseTrigger

class _StateDict(TypedDict):
  version: int
  triggers: list[tuple[str, dict]]
  jitter: int | None

class BaseCombiningTrigger(BaseTrigger, metaclass=abc.ABCMeta):
  __slots__ = ("jitter", "triggers")
  triggers: list[BaseTrigger]
  jitter: int | None
  def __init__(self, triggers: list[BaseTrigger], jitter: int | None = None) -> None: ...
  def __getstate__(self) -> _StateDict: ...
  def __setstate__(self, state: _StateDict) -> None: ...

class AndTrigger(BaseCombiningTrigger):
  def get_next_fire_time(self, previous_fire_time: datetime | None, now: datetime) -> datetime | None: ...

class OrTrigger(BaseCombiningTrigger):
  def get_next_fire_time(self, previous_fire_time: datetime | None, now: datetime) -> datetime | None: ...
