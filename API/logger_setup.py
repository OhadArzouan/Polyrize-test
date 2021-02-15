# Standard packages
import logging
from sys import stdout, stderr

logging.getLogger('sanic').setLevel(logging.WARNING)

_instance = None


def setup_logging(log_lvl='INFO', logger_name='global'):
    global _instance
    if not _instance:
        _instance = {}
    _logger = logging.getLogger(logger_name)
    for h in _logger.handlers:
        _logger.removeHandler(h)
    _logger.propagate = False
    _format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    h = logging.StreamHandler(stdout)
    h.setFormatter(logging.Formatter(_format))
    _logger.addHandler(h)
    h_err = logging.StreamHandler(stderr)
    h_err.setLevel(logging.ERROR)
    h_err.setFormatter(logging.Formatter(_format))
    _logger.addHandler(h_err)
    _logger.setLevel(logging.getLevelName(log_lvl))

    _instance[logger_name] = _logger
    return _instance[logger_name]
