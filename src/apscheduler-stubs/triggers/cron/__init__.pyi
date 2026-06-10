# Standard library imports
from datetime import datetime, timezone
from typing import Literal, TypedDict
from zoneinfo import ZoneInfo

# Third party imports
from _typeshed import Incomplete
from apscheduler.triggers.base import BaseTrigger
from apscheduler.triggers.cron.fields import BaseField, DayOfMonthField, DayOfWeekField, MonthField, WeekField

UTC: Incomplete

type _FieldCatchAll = BaseField | DayOfMonthField | DayOfWeekField | MonthField | WeekField

class _FieldsMap(TypedDict):
  year: BaseField
  month: MonthField
  week: WeekField
  day: DayOfMonthField
  day_of_week: DayOfWeekField
  hour: BaseField
  minute: BaseField
  second: BaseField

class _StateDict(TypedDict):
  version: int
  timezone: ZoneInfo | timezone
  start_date: datetime | None
  end_date: datetime | None
  fields: list[_FieldCatchAll]
  jitter: int | None

class CronTrigger(BaseTrigger):
  FIELD_NAMES: tuple[
    Literal["year"],
    Literal["month"],
    Literal["day"],
    Literal["week"],
    Literal["day_of_week"],
    Literal["hour"],
    Literal["minute"],
    Literal["second"],
  ]
  FIELDS_MAP: _FieldsMap
  timezone: ZoneInfo | timezone
  start_date: datetime | None
  end_date: datetime | None
  jitter: int | None
  fields: list[_FieldCatchAll]
  def __init__(
    self,
    year: int | str | None = None,
    month: int | str | None = None,
    day: int | str | None = None,
    week: int | str | None = None,
    day_of_week: int | str | None = None,
    hour: int | str | None = None,
    minute: int | str | None = None,
    second: int | str | None = None,
    start_date: datetime | str | None = None,
    end_date: datetime | str | None = None,
    timezone: ZoneInfo | timezone | None = None,
    jitter: int | None = None,
  ) -> None: ...
  @classmethod
  def from_crontab(cls, expr: str, timezone: ZoneInfo | timezone | None = None) -> CronTrigger: ...
  def _increment_field_value(self, dateval: datetime, fieldnum: int) -> tuple[datetime, int]: ...
  def _set_field_value(self, dateval: datetime, fieldnum: int, new_value: int) -> datetime: ...
  def get_next_fire_time(self, previous_fire_time: datetime | None, now: datetime) -> datetime | None: ...
  def __getstate__(self) -> _StateDict: ...
  def __setstate__(self, state: _StateDict) -> None: ...
