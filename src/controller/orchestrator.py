import pandas as pd

from ..data import DbConnect
from ..models import FundamentusModel, TickerModel
from ..robot import Downloader
from ..utils import DataInterpreter
from ..core import logger



class Orchestrator:

    def __init__(self) -> None:
        self.db = DbConnect()

    def perform_workflow(self):
        table_str = Downloader.fundamentus()

        df = DataInterpreter.fundamentus(table_str)
        self.upsert_new_tickers(df)
        self.db.upsert(df, FundamentusModel)

    def upsert_new_tickers(self, df: pd.DataFrame):
        to_insert = self.get_tickers_to_insert(df)

        if to_insert:
            logger.info("Cadastrando novos tickers")
            df_to_insert = df[
                ["ticker_id"]
            ].drop_duplicates(["ticker_id"])
            df_to_insert = (
                df_to_insert[df_to_insert["ticker_id"].isin(to_insert)]
                .rename(columns={"ticker_id": "id"})
                .reset_index(drop=True)
            )
            self.db.upsert(df_to_insert, model=TickerModel)

    def get_tickers_to_insert(self, df: pd.DataFrame) -> list[str]:
        registered_tickers = [record.id for record in self.db.get_tickers()]
        current_tickers = df["ticker_id"].unique().tolist()

        return [
            str(ticker)
            for ticker in current_tickers
            if ticker not in registered_tickers
        ]
