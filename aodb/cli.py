

import click

from .main import generate_exports, compress_exports, upload_exports, clean_output_folder, generate_basic_scheme


@click.group()
@click.pass_context
def cli(ctx):
    pass


@cli.command()
@click.option('-v', '--version', required=True, type=str, help='The version number to label the output with.')
@click.option('-c', '--clean', is_flag=True, default=False, help='Remove the contents of the output folder first.')
@click.pass_context
def generate(ctx, version: str, clean: bool):
    """CLI wrapper for the main generate function."""
    if clean:
        clean_output_folder()

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


@cli.command()
@click.pass_context
def scheme(ctx):
    generate_basic_scheme()
