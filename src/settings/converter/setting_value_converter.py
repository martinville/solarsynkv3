from csv import DictReader
from pathlib import Path


class SettingValueConverter:
    def __init__(self, setting_value_map=None):
        if setting_value_map is None:
            setting_value_map = {}

            with open(Path(__file__).parent.parent / 'resources' / 'setting_types.csv', 'r') as reader:
                dict_reader = DictReader(reader)

                for row in dict_reader:
                    setting_name = row['name']
                    setting_value_map[setting_name] = row['type']

        self.setting_value_map = setting_value_map

    def convert_value(self, key, value):
        # get the expected type for this setting
        setting_type = self.setting_value_map.get(key, None)

        # perform the conversion
        if setting_type == 'bool':
            if value == 't':
                return 'true'
            if value == 'f':
                return 'false'

        return value