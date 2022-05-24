from datetime import datetime
import sys

import click
from loguru import logger


@click.command(
    context_settings=dict(
        help_option_names=["-h", "--help"],
    ),
    options_metavar="<options>",
)
@click.option(
    "--working-directory",
    help="Download directory",
    type=click.Path(),
    default="./ipgcor-data",
    metavar="<directory>",
)
@click.option(
    "--authentication-file",
    help="File containing authentication information",
    metavar="<secrets file>",
    default="./ipgcor-secrets"
)
@click.version_option()
def main(working_directory, authentication_file):
    start = datetime.utcnow()
    setup_logging()
    logger.info("Program start.")
    logger.info(f"{dict(working_directory=working_directory)}")
    logger.info(f"{dict(authentication_file=authentication_file)}")
    # correlate_things()
    end = datetime.utcnow()
    logger.info(f"Program end after: {end - start}")

def setup_logging():
    logger.remove()
    logger.add(
        sys.stderr,
        level="INFO",
        format=("<green>{time:YYYY-MM-DDTHH:mm:ss.SSS!UTC}Z</green> "
                "| <level>{level: <8}</level> "
                "| <cyan>{name}</cyan>:<cyan>{function}</cyan>:"
                "<cyan>{line}</cyan> "
                "- <level>{message}</level>")
    )

main()
