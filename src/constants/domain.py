from enum import Enum

FUNDAMENTUS_URL = "https://www.fundamentus.com.br/resultado.php"


class Browser(Enum):

    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) "
            "Gecko/20100101 Firefox/120.0"
        )
    }


class FundamentusColumns(Enum):

    MAPPING = {
        "Papel": "ticker_id",
        "Cotação": "price",
        "P/L": "pe_ratio",
        "P/VP": "pb_ratio",
        "PSR": "ps_ratio",
        "Div.Yield": "dividend_yield",
        "P/Ativo": "price_to_assets",
        "P/Cap.Giro": "price_to_working_capital",
        "P/EBIT": "price_to_ebit",
        "P/Ativ Circ.Liq": "price_to_net_current_assets",
        "EV/EBIT": "ev_to_ebit",
        "EV/EBITDA": "ev_to_ebitda",
        "Mrg Bruta": "gross_margin",
        "Mrg Ebit": "ebit_margin",
        "Mrg. Líq.": "net_margin",
        "Liq. Corr.": "current_ratio",
        "ROIC": "roic",
        "ROE": "roe",
        "Liq.2meses": "average_daily_volume_2m",
        "Patrim. Líq": "net_worth",
        "Dív.Líq/ Patrim.": "net_debt_to_equity",
        "Cresc. Rec.5a": "revenue_growth_5y",
    }


    PERCENTAGE_COLS = [
        "dividend_yield",
        "gross_margin",
        "ebit_margin",
        "net_margin",
        "roic",
        "roe",
        "revenue_growth_5y"
    ]