import logging

def setup_logger():
    """
    Configure the global logger for the entire project.
    Sets the message output format and the logging level.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )