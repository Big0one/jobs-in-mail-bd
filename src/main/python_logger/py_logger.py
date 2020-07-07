import logging


class PyLogger:
    @staticmethod
    def get_logger():
        msg_fmt = "[%(asctime)s ] %(levelname)s @ line %(lineno)d: %(message)s"
        logging.basicConfig(level=logging.DEBUG, format=msg_fmt)
        return logging.getLogger(__name__)


if __name__ == "__main__":
    logger = PyLogger.get_logger()
    logger.info("info")
