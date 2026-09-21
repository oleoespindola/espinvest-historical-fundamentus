import logging
import os
from logging.handlers import TimedRotatingFileHandler


class Logging:
    """Configures and manages application-level logging with daily rotation."""

    def __init__(self) -> None:
        self.log_dir = os.path.join(".", "log")
        os.makedirs(self.log_dir, exist_ok=True)

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:
            self._setup_handlers()

    def _setup_handlers(self) -> None:
        log_format = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(module)s - %(funcName)s: %(message)s"
        )

        file_handler = TimedRotatingFileHandler(
            filename=os.path.join(self.log_dir, "app.log"),
            when="D",
            interval=1,
            backupCount=7,
            encoding="utf-8",
        )
        file_handler.setFormatter(log_format)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_format)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_logger(self) -> logging.Logger:
        return self.logger


logger = Logging().get_logger()
