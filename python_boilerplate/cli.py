"""Console script for python_boilerplate."""
import sys

import click


@click.command()
def main(*args):
    """
    Console script for python_boilerplate.

    :param args: A list of args to pass.
    :type args: Optional[list]

    :return: A status message
    :rtype: int
    """
    len(args)
    click.echo(
        "Replace this message by putting your code into " "python_boilerplate.cli.main"
    )
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
