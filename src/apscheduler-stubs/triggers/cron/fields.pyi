# Standard library imports
from datetime import datetime
from typing import ClassVar, Literal, TypedDict

# Third party imports
from apscheduler.triggers.cron.expressions import (
  AllExpression,
  LastDayOfMonthExpression,
  MonthRangeExpression,
  RangeExpression,
  WeekdayPositionExpression,
  WeekdayRangeExpression,
)

__all__ = ["DEFAULT_VALUES", "MAX_VALUES", "MIN_VALUES", "BaseField", "DayOfMonthField", "DayOfWeekField", "WeekField"]

class _MinValues(TypedDict):
  year: Literal[1970]
  month: Literal[1]
  day: Literal[1]
  week: Literal[1]
  day_of_week: Literal[0]
  hour: Literal[0]
  minute: Literal[0]
  second: Literal[0]

class _MaxValues(TypedDict):
  year: Literal[9999]
  month: Literal[12]
  day: Literal[31]
  week: Literal[53]
  day_of_week: Literal[6]
  hour: Literal[23]
  minute: Literal[59]
  second: Literal[59]

class _DefaultValues(TypedDict):
  year: Literal["*"]
  month: Literal[1]
  day: Literal[1]
  week: Literal["*"]
  day_of_week: Literal["*"]
  hour: Literal[0]
  minute: Literal[0]
  second: Literal[0]

MIN_VALUES: _MinValues
MAX_VALUES: _MaxValues
DEFAULT_VALUES: _DefaultValues

class BaseField[ExprTypes_T: AllExpression = AllExpression | RangeExpression]:
  REAL: ClassVar[bool]
  COMPILERS: list[type[ExprTypes_T]]
  name: Literal["year", "month", "day", "week", "day_of_week", "hour", "minute", "second"]
  is_default: bool
  def __init__(
    self,
    name: Literal["year", "month", "day", "week", "day_of_week", "hour", "minute", "second"],
    exprs: str | int,
    is_default: bool = False,
  ) -> None: ...
  def get_min(self, dateval: datetime) -> int | str: ...
  def get_max(self, dateval: datetime) -> int | str: ...
  def get_value(self, dateval: datetime) -> int: ...
  def get_next_value(self, dateval: datetime): ...
  expressions: list[ExprTypes_T]
  def compile_expressions(self, exprs: str) -> None: ...
  def compile_expression(self, expr: str) -> None: ...
  def __eq__(self, other: object) -> bool: ...

class WeekField(BaseField):
  REAL: ClassVar[bool]
  def get_value(self, dateval: datetime) -> int: ...

class DayOfMonthField(BaseField[AllExpression | RangeExpression | WeekdayPositionExpression | LastDayOfMonthExpression]):
  def get_max(self, dateval: datetime) -> int: ...

class DayOfWeekField(BaseField[AllExpression | RangeExpression | WeekdayRangeExpression]):
  REAL: ClassVar[bool]
  def get_value(self, dateval: datetime) -> int: ...

class MonthField(BaseField[AllExpression | RangeExpression | MonthRangeExpression]): ...
