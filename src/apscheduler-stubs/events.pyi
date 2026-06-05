from _typeshed import Incomplete

__all__ = [
  "EVENT_ALL",
  "EVENT_ALL_JOBS_REMOVED",
  "EVENT_EXECUTOR_ADDED",
  "EVENT_EXECUTOR_REMOVED",
  "EVENT_JOBSTORE_ADDED",
  "EVENT_JOBSTORE_REMOVED",
  "EVENT_JOB_ADDED",
  "EVENT_JOB_ERROR",
  "EVENT_JOB_EXECUTED",
  "EVENT_JOB_MAX_INSTANCES",
  "EVENT_JOB_MISSED",
  "EVENT_JOB_MODIFIED",
  "EVENT_JOB_REMOVED",
  "EVENT_JOB_SUBMITTED",
  "EVENT_SCHEDULER_PAUSED",
  "EVENT_SCHEDULER_RESUMED",
  "EVENT_SCHEDULER_SHUTDOWN",
  "EVENT_SCHEDULER_STARTED",
  "JobEvent",
  "JobExecutionEvent",
  "JobSubmissionEvent",
  "SchedulerEvent",
]

EVENT_SCHEDULER_STARTED: int
EVENT_SCHEDULER_SHUTDOWN: int
EVENT_SCHEDULER_PAUSED: int
EVENT_SCHEDULER_RESUMED: int
EVENT_EXECUTOR_ADDED: int
EVENT_EXECUTOR_REMOVED: int
EVENT_JOBSTORE_ADDED: int
EVENT_JOBSTORE_REMOVED: int
EVENT_ALL_JOBS_REMOVED: int
EVENT_JOB_ADDED: int
EVENT_JOB_REMOVED: int
EVENT_JOB_MODIFIED: int
EVENT_JOB_EXECUTED: int
EVENT_JOB_ERROR: int
EVENT_JOB_MISSED: int
EVENT_JOB_SUBMITTED: int
EVENT_JOB_MAX_INSTANCES: int
EVENT_ALL = (  # noqa: PYI026
  EVENT_SCHEDULER_STARTED
  | EVENT_SCHEDULER_SHUTDOWN
  | EVENT_SCHEDULER_PAUSED
  | EVENT_SCHEDULER_RESUMED
  | EVENT_EXECUTOR_ADDED
  | EVENT_EXECUTOR_REMOVED
  | EVENT_JOBSTORE_ADDED
  | EVENT_JOBSTORE_REMOVED
  | EVENT_ALL_JOBS_REMOVED
  | EVENT_JOB_ADDED
  | EVENT_JOB_REMOVED
  | EVENT_JOB_MODIFIED
  | EVENT_JOB_EXECUTED
  | EVENT_JOB_ERROR
  | EVENT_JOB_MISSED
  | EVENT_JOB_SUBMITTED
  | EVENT_JOB_MAX_INSTANCES
)

class SchedulerEvent:
  code: Incomplete
  alias: Incomplete
  def __init__(self, code, alias=None) -> None: ...
  def __repr__(self) -> str: ...

class JobEvent(SchedulerEvent):
  code: Incomplete
  job_id: Incomplete
  jobstore: Incomplete
  def __init__(self, code, job_id, jobstore) -> None: ...

class JobSubmissionEvent(JobEvent):
  scheduled_run_times: Incomplete
  def __init__(self, code, job_id, jobstore, scheduled_run_times) -> None: ...

class JobExecutionEvent(JobEvent):
  scheduled_run_time: Incomplete
  retval: Incomplete
  exception: Incomplete
  traceback: Incomplete
  def __init__(self, code, job_id, jobstore, scheduled_run_time, retval=None, exception=None, traceback=None) -> None: ...
