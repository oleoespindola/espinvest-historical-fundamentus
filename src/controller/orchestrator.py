from ..data import DbConnect
from ..models import FundamentusModel
from ..robot import Downloader
from ..utils import DataInterpreter


class Orchestrator:

    def __init__(self) -> None:
        self.db = DbConnect()

    def perform_workflow(self):
        table_str = Downloader.fundamentus()

        df = DataInterpreter.fundamentus(table_str)
        self.db.upsert(df, FundamentusModel)
