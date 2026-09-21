from io import StringIO

import pandas as pd

from ..constants import FundamentusColumns


class DataInterpreter:

    @staticmethod
    def fundamentus(table: StringIO) -> pd.DataFrame:
        df = pd.read_html(table, decimal=",", thousands=".")[0]

        df.rename(columns=FundamentusColumns.MAPPING.value, inplace=True)

        for col in df.columns:
            if col == "ticker_id":
                df[col] = df[col].astype(str).str.strip()

            else:
                is_pct = col in FundamentusColumns.PERCENTAGE_COLS.value
                df[col] = df[col].apply(
                    lambda x: DataInterpreter._clean_numeric_value(x, is_pct)
                )

        return df

    @staticmethod
    def _clean_numeric_value(val, is_percentage: bool = False):
        if pd.isna(val) or val == "-":
            return None

        if isinstance(val, str):
            val = val.replace(".", "").replace(",", ".").replace("%", "").strip()

        try:
            parsed_val = float(val)
            return parsed_val / 100.0 if is_percentage else parsed_val

        except ValueError:
            return None  # TODO:
