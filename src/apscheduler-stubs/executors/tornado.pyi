from _typeshed import Incomplete
from apscheduler.executors.base import BaseExecutor as BaseExecutor, run_coroutine_job as run_coroutine_job, run_job as run_job
from apscheduler.util import iscoroutinefunction_partial as iscoroutinefunction_partial

class TornadoExecutor(BaseExecutor):
    executor: Incomplete
    def __init__(self, max_workers: int = 10) -> None: ...
    _ioloop: Incomplete
    def start(self, scheduler, alias) -> None: ...
    def _do_submit_job(self, job, run_times) -> None: ...
