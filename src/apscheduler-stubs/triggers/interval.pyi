# Standard library imports
from datetime import date, datetime, timedelta, timezone
from typing import TypedDict
from zoneinfo import ZoneInfo

# Third party imports
from apscheduler.triggers.base import BaseTrigger

class _StateDict(TypedDict):
  version: int
  timezone: ZoneInfo | timezone
  start_date: datetime | None
  end_date: datetime | None
  interval: timedelta
  jitter: int | None

class IntervalTrigger(BaseTrigger):
  __slots__ = (
    "end_date",
    "interval",
    "interval_length",
    "jitter",
    "start_date",
    "timezone",
  )
  interval: timedelta
  interval_length: float
  timezone: ZoneInfo | timezone
  start_date: datetime | None
  end_date: datetime | None
  jitter: int | None
  def __init__(
    self,
    weeks: int = 0,
    days: int = 0,
    hours: int = 0,
    minutes: int = 0,
    seconds: int = 0,
    start_date: datetime | date | str | None = None,
    end_date: datetime | date | str | None = None,
    timezone: ZoneInfo | timezone | None = None,
    jitter: int | None = None,
  ) -> None: ...
  def get_next_fire_time(self, previous_fire_time: datetime | None, now: datetime) -> datetime | None: ...
  def __getstate__(self) -> _StateDict: ...
  def __setstate__(self, state: _StateDict) -> None: ...
