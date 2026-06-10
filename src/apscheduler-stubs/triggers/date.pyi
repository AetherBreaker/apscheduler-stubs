# Standard library imports
from datetime import date, datetime, timezone
from typing import TypedDict
from zoneinfo import ZoneInfo

# Third party imports
from apscheduler.triggers.base import BaseTrigger

class _StateDict(TypedDict):
  version: int
  run_date: datetime

class DateTrigger(BaseTrigger):
  run_date: datetime
  def __init__(self, run_date: datetime | date | str | None = None, timezone: ZoneInfo | timezone | None = None) -> None: ...
  def get_next_fire_time(self, previous_fire_time: datetime | None, now: datetime) -> datetime | None: ...
  def __getstate__(self) -> _StateDict: ...
  def __setstate__(self, state: _StateDict) -> None: ...
