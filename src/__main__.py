from datetime import datetime

import click
from loguru import logger

from .correlate import correlate_things

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
    logger.info("Program start.")
    logger.info(f"{dict(working_directory=working_directory)}")
    logger.info(f"{dict(authentication_file=authentication_file)}")
    correlate_things()
    end = datetime.utcnow()
    logger.info(f"Program end after: {end - start}")

main()
