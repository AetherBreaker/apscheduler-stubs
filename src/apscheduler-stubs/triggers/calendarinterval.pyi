# Standard library imports
from datetime import date, datetime, time, timezone, tzinfo
from typing import TypedDict
from zoneinfo import ZoneInfo

# Third party imports
from apscheduler.triggers.base import BaseTrigger

class _StateDict(TypedDict):
  version: int
  interval: list[int]
  time: list[int]
  start_date: date
  end_date: date | None
  timezone: ZoneInfo | timezone | tzinfo
  jitter: int | None

class CalendarIntervalTrigger(BaseTrigger):
  __slots__ = (
    "_time",
    "days",
    "end_date",
    "jitter",
    "months",
    "start_date",
    "timezone",
    "weeks",
    "years",
  )
  timezone: ZoneInfo | timezone | tzinfo
  years: int
  months: int
  weeks: int
  days: int
  start_date: date
  end_date: date | None
  jitter: int | None
  _time: time
  def __init__(
    self,
    *,
    years: int = 0,
    months: int = 0,
    weeks: int = 0,
    days: int = 0,
    hour: int = 0,
    minute: int = 0,
    second: int = 0,
    start_date: date | str | None = None,
    end_date: date | str | None = None,
    timezone: str | tzinfo | None = None,
    jitter: int | None = None,
  ) -> None: ...
  def get_next_fire_time(self, previous_fire_time: datetime | None, now: datetime) -> datetime | None: ...
  def __getstate__(self) -> _StateDict: ...
  def __setstate__(self, state: _StateDict) -> None: ...
