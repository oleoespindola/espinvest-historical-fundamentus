from contextlib import contextmanager
from typing import Any, Generator, Hashable

import numpy as np
import pandas as pd
from sqlalchemy import URL, Table, create_engine
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import SQLAlchemyError, TimeoutError
from sqlalchemy.orm import Session, sessionmaker

from ..core import get_settings, logger
from ..models import FundamentusModel

settings = get_settings()

database_url = URL.create(
    drivername="postgresql+psycopg2",
    username=settings.DATABASE_USER,
    password=settings.DATABASE_PASSWORD,
    host=settings.DATABASE_HOST,
    port=settings.DATABASE_PORT,
    database=settings.DATABASE_NAME,
)

engine = create_engine(database_url)

SessionLocal = sessionmaker(
    bind=engine, autoflush=False, autocommit=False, expire_on_commit=False
)


@contextmanager
def get_connection() -> Generator[Session, None, None]:
    session = SessionLocal()

    try:
        logger.info("Abrindo conexão com o banco de dados")
        yield session

        session.commit()

    except Exception as exc:
        if isinstance(exc, SQLAlchemyError):
            logger.critical(
                "Erro ao realizar operação no banco de dados", exc_info=True
            )

        elif isinstance(exc, TimeoutError):
            logger.critical(
                "Tempo excedido ao tentar se conectar com o banco de dados",
                exc_info=True,
            )

        logger.critical("Realizando rollback das operações")
        session.rollback()

        raise exc

    finally:
        logger.info("Encerrando conexão com o banco de dados")
        session.close()


class DbConnectException(Exception):

    def __init__(self, message: str) -> None:
        super().__init__(message)


class DbConnect:

    def upsert(
        self,
        df: pd.DataFrame,
        model: type[FundamentusModel],
    ) -> None:
        logger.info(
            f"Inserindo informações no banco de dados; tabela {model.__tablename__}"
        )

        try:
            clean_df = df.replace({np.nan: None})
            records: list[dict[Hashable, Any]] = clean_df.to_dict(orient="records")
            del df, clean_df

            if not records:
                return

            table: Table = model.__table__

            statement = insert(table).values(records)

            update_columns = {
                column.name: statement.excluded[column.name]
                for column in table.columns
                if column.name != "ticker_id"
            }

            statement = statement.on_conflict_do_update(
                index_elements=[table.c.id, table.c.ticker_id],
                set_=update_columns,
            )

            with get_connection() as conn:
                conn.execute(statement)

        except Exception as exc:
            message: str = "Erro a inserir/atualizar informações no banco de dados"

            logger.critical(message, exc_info=True)
            raise DbConnectException(message) from exc
