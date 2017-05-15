

import re

from json import dump
from xmljson import gdata
from xml.etree import ElementTree

from .base import BaseExporter


class JSONExporter(BaseExporter):
    def _generate_export(self):
        export_file = self.export_file.format('json')

        clean = re.sub(
            r' xmlns:xsi="http:\/\/www\.w3\.org\/2001\/XMLSchema-instance" xsi:noNamespaceSchemaLocation=".*\.xsd"',
            '',
            self.input
        )

        json = gdata.data(ElementTree.fromstring(clean))

        with open(export_file, 'w') as out_file:
            dump(json, out_file, indent=4)

    def generate_basic_scheme(self):
        self._load_input()

        clean = re.sub(
            r' xmlns:xsi="http:\/\/www\.w3\.org\/2001\/XMLSchema-instance" xsi:noNamespaceSchemaLocation=".*\.xsd"',
            '',
            self.input
        )

        json = gdata.data(ElementTree.fromstring(clean))

        for input_name, input_values in json.items():
            if input_name == 'items':
                for table_name, table_values in input_values.items():
                    scheme = {}
                    skipped = set()
                    conflicts = set()

                    for row in table_values:
                        for name, value in row.items():
                            if isinstance(value, str):
                                type_name = 'STRING'

                            elif isinstance(value, float):
                                type_name = 'FLOAT'

                            elif isinstance(value, bool):
                                type_name = 'BOOLEAN'

                            elif isinstance(value, int):
                                type_name = 'INTEGER'

                            else:
                                skipped.add((name, type(value)))
                                continue

                            if name not in scheme.keys():
                                scheme[name] = type_name

                            elif scheme[name] == 'INTEGER' and type_name == 'FLOAT':
                                scheme[name] = type_name

                            elif scheme[name] == 'FLOAT' and type_name == 'INTEGER':
                                continue

                            elif scheme[name] != type_name:
                                conflicts.add((name, scheme[name], type_name))

                    print('')
                    print('')
                    print(f'### TABLE {table_name} ###')
                    print('### Scheme')
                    for k, v in scheme.items():
                        print(f'{k} {v},')

                    print('')
                    print('### Conflicts')
                    print(conflicts)

                    print('')
                    print('### Skipped')
                    print(skipped)
