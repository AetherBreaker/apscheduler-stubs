from datetime import datetime, timezone
from typing import Any, Self
from apscheduler.executors.base import BaseExecutor
from apscheduler.schedulers.base import BaseScheduler
from apscheduler.triggers.base import BaseTrigger
from collections.abc import Callable, Sequence

UTC: timezone

class Job:
  _scheduler: BaseScheduler
  _jobstore_alias: str
  def __init__(self, scheduler: BaseScheduler, id: str | None = None, **kwargs) -> None: ...  # noqa: A002
  def modify(self, **changes) -> Self: ...
  def reschedule(self, trigger: BaseTrigger, **trigger_args) -> Self: ...
  def pause(self) -> Self: ...
  def resume(self) -> Self: ...
  def remove(self) -> None: ...
  @property
  def pending(self) -> bool: ...
  def _get_run_times(self, now: datetime) -> list[datetime]: ...
  def _modify(self, **changes) -> None: ...
  def __getstate__(self) -> dict[str, Any]: ...
  id: str
  func_ref: str
  func: Callable[..., Any]
  trigger: BaseTrigger
  executor: BaseExecutor
  args: Sequence[Any]
  kwargs: dict[str, Any]
  name: str
  misfire_grace_time: int
  coalesce: bool
  max_instances: int
  next_run_time: datetime
  def __setstate__(self, state: dict[str, Any]) -> None: ...
  def __eq__(self, other: object) -> bool: ...
