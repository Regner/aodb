

import click

from .main import generate_exports, compress_exports, upload_exports


@click.group()
@click.pass_context
def cli(ctx):
    pass


@cli.command()
@click.option('-v', '--version', required=True, type=str, help='The version number to label the output with.')
@click.pass_context
def generate(ctx, version: str):
    """CLI wrapper for the main generate function."""
    generate_exports(version)


@cli.command()
@click.option('-v', '--version', required=True, type=str, help='The version number to label the output with.')
@click.pass_context
def compress(ctx, version: str):
    """CLI wrapper for the main compress function."""
    compress_exports(version)


@cli.command()
@click.option('-v', '--version', required=True, type=str, help='The version number to label the output with.')
@click.option('-b', '--bucket', required=True, type=str, help='The bucket to upload the files to.')
@click.pass_context
def upload(ctx, version: str, bucket: str):
    """CLI wrapper for the main upload function."""
    upload_exports(version, bucket)
