import logging

from datetime import datetime

import json

import sys


def initialize_logging(level="DEBUG", log_file=None, to_stdout=True, add_trace=False):
    handlers = []

    if to_stdout:
        handlers.append(logging.StreamHandler(sys.stdout))

    if log_file is not None:
        handlers.append(_get_filehandler(log_file))

    logging.basicConfig(
        handlers=handlers,
        level=getattr(logging, level),
        format="%(message)s",
    )


def get_logger(name=None):
    """Initialize the root logger for the module."""
    if name is not None:
        logger = logging.getLogger(name)
    else:
        logger = logging.getLogger(__package__)
    return logger


def _get_filehandler(file_path=None):
    logfile_handler = logging.FileHandler(file_path)
    logfile_handler.formatter = StructuredFormatter()
    return logfile_handler


def struct_msg(message: str, **kwargs) -> dict:
    """Creates and returns a structured log message"""
    out = {"message": message}
    out.update(**kwargs)
    return out


class StructuredFormatter(logging.Formatter):
    def format(self, record):
        out = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
        }
        if type(record.msg) == str:
            out["message"] = record.msg
        else:
            out.update(record.msg)

        if record.levelno in [logging.ERROR, logging.DEBUG, logging.CRITICAL]:
            out["debug_info"] = {
                "module": record.module,
                "funcName": record.funcName,
                "filename": record.filename,
                "pathname": record.pathname,
                "lineno": record.lineno,
            }
        return json.dumps(out)

    def formatTime(self, record):
        return datetime.fromtimestamp(record.created).astimezone().isoformat()
