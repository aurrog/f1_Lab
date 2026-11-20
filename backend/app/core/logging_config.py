import logging
from pathlib import Path
from logging.handlers import RotatingFileHandler


def setup_logging():
    logs_dir=Path('logs')
    logs_dir.mkdir(exist_ok=True)

    formatter=logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
    file_handler=RotatingFileHandler(
        logs_dir / 'app.log',
        maxBytes=5*1024*1024,
        backupCount=3,
        encoding='utf-8',
    )
    file_handler.setFormatter(formatter)

    console_handler=logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[file_handler, console_handler],
    )
