#open up the swarms class to intake external tooks like Swarm(tool)
import traceback
import logging 
from swarms import Swarms

api_key = "your-api-key-here"
swarm = Swarms(openai_api_key=api_key)


logging.basicConfig(filename="app.log", level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


def log_exception(exc):
    #capture the tracback with the exception
    tb_lines = traceback.format_exception(exc.__class__, exc, exc.__traceback__)
    tb_text = ''.join(tb_lines)

    #log the exception 
    logging.error("Caught an exception", tb_text)


def handle_exception(exc):
    log_exception(exc)

    #running swarms on exception
    response = swarm.run_swarms(f"Interpret this error:\n{str(exc)}")

    #todo handle the exception based on the swarms response