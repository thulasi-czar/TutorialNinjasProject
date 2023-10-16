import logging

class LogGenerator:
    @staticmethod
    def gen_logs():
        logger = logging.getLogger(__name__)
        fh = logging.FileHandler(".\\logs\\automation.log")
        log_format = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s",datefmt="%d/%m/%Y %I:%M:%S %p")
        fh.setFormatter(log_format)
        logger.addHandler(fh)
        logger.setLevel(logging.INFO)
        return logger