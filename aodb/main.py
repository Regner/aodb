

import shutil
import tarfile

from os import makedirs, listdir
from os.path import exists, isfile, join
from google.cloud import storage
from collections import defaultdict

from . import exporters
from .resources import RESOURCES


DEFAULT_INPUT = 'inputs/'
DEFAULT_OUTPUT = 'outputs/'


def get_input_path(name: str, input_folder: str = DEFAULT_INPUT) -> str:
    file_name = f'{name}.txt'
    return join(input_folder, file_name)


def get_output_version_folder(version: str, output_folder: str = DEFAULT_OUTPUT) -> str:
    return join(output_folder, version)


def get_output_path(name: str, version: str, output_folder) -> str:
    file_name = f'{version}-{name}.' + '{}'
    return join(output_folder, file_name)


def run_exporter(exporter, input_path: str, output_path: str):
    exporter(input_path, output_path).generate_export()


def generate_exports(version: str):
    """Generates the database conversions."""
    print('Generating exports...')

    output_folder = get_output_version_folder(version)
    if not exists(output_folder):
        makedirs(output_folder)

    for resource in RESOURCES:
        name = resource['name']
        print(f'Exporting {name}...')

        input_path = get_input_path(name)
        output_path = get_output_path(name, version, output_folder)

        for exporter in exporters.base_exporters:
            run_exporter(exporter, input_path, output_path)

        for exporter in resource['custom_exporters']:
            run_exporter(exporter, input_path, output_path)


def compress_exports(version: str):
    """Groups and compresses all the files based on file extension."""
    print('Compressing exported files...')

    files_by_extension = defaultdict(list)
    folder_path = get_output_version_folder(version)

    for file in listdir(folder_path):
        full_path = join(folder_path, file)

        if isfile(full_path):
            extension = file.split('.')[-1]

            if extension != 'gz':
                files_by_extension[extension].append(full_path)

    for extension, files in files_by_extension.items():
        print(f'Compressing {extension} files now...')

        full_path = join(folder_path, f'{version}-{extension}.tar.gz')

        with tarfile.open(full_path, 'w:gz') as out_file:
            for file in files:
                out_file.add(file)


def upload_exports(version: str, bucket_name: str):
    """Uploads all the compressed exports to Google Cloud Storage."""
    print('Uploading compressed exports to Google Cloud Storage...')

    client = storage.Client()
    bucket = client.get_bucket(bucket_name)

    folder_path = get_output_version_folder(version)

    for file in listdir(folder_path):
        if file.endswith('.gz'):
            blob = storage.Blob(file, bucket)

            full_path = join(folder_path, file)

            with open(full_path, 'rb') as in_file:
                print(f'Uploading {full_path} to {bucket_name}...')
                blob.upload_from_file(in_file)


def clean_output_folder():
    """Removes the contents of the output folder."""
    if exists(DEFAULT_OUTPUT):
        shutil.rmtree(DEFAULT_OUTPUT)


def generate_basic_scheme():
    for resource in RESOURCES:
        name = resource['name']
        print(f'Creating basic scheme for {name}...')

        input_path = get_input_path(name)

        exporter = exporters.JSONExporter(input_path, '')
        exporter.generate_basic_scheme()
