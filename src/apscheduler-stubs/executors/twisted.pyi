from _typeshed import Incomplete
from apscheduler.executors.base import BaseExecutor as BaseExecutor, run_job as run_job

class TwistedExecutor(BaseExecutor):
    _reactor: Incomplete
    def start(self, scheduler, alias) -> None: ...
    def _do_submit_job(self, job, run_times) -> None: ...
