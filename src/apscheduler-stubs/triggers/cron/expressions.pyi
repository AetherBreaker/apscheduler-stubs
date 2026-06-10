# Standard library imports
from datetime import datetime
from re import Pattern

# Third party imports
from _typeshed import ConvertibleToInt
from apscheduler.triggers.cron.fields import BaseField

__all__ = ["AllExpression", "LastDayOfMonthExpression", "RangeExpression", "WeekdayPositionExpression", "WeekdayRangeExpression"]

class AllExpression:
  value_re: Pattern
  step: int | None
  def __init__(self, step: ConvertibleToInt | None = None) -> None: ...
  def validate_range(self, field_name: str) -> None: ...
  def get_next_value(self, date: datetime, field: BaseField): ...
  def __eq__(self, other: object) -> bool: ...

class RangeExpression(AllExpression):
  value_re: Pattern
  first: int | None
  last: int | None
  def __init__(
    self, first: ConvertibleToInt | None, last: ConvertibleToInt | None = None, step: ConvertibleToInt | None = None
  ) -> None: ...
  def validate_range(self, field_name: str) -> None: ...
  def get_next_value(self, date: datetime, field: BaseField) -> int | None: ...
  def __eq__(self, other: object) -> bool: ...

class MonthRangeExpression(RangeExpression):
  value_re: Pattern
  def __init__(self, first: str, last: str | None = None) -> None: ...

class WeekdayRangeExpression(RangeExpression):
  value_re: Pattern
  def __init__(self, first: str, last: str | None = None) -> None: ...

class WeekdayPositionExpression(AllExpression):
  options: list[str]
  value_re: Pattern
  option_num: int
  weekday: int
  def __init__(self, option_name: str, weekday_name: str) -> None: ...
  def get_next_value(self, date: datetime, field: BaseField) -> int | None: ...
  def __eq__(self, other: object) -> bool: ...

class LastDayOfMonthExpression(AllExpression):
  value_re: Pattern
  def __init__(self) -> None: ...
  def get_next_value(self, date: datetime, field: BaseField) -> int: ...
