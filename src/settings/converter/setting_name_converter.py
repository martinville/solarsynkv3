from csv import DictReader
from pathlib import Path


class SettingNameConverter:
    def __init__(self, setting_name_map=None):
        if setting_name_map is None:
            setting_name_map = {}

            with open(Path(__file__).parent.parent / 'resources' / 'setting_names.csv', 'r') as reader:
                dict_reader = DictReader(reader)

                for row in dict_reader:
                    setting_name = row['name']
                    setting_name_map[row['short_name']] = setting_name

        self.setting_name_map = setting_name_map

    def convert_name(self, key):
        return self.setting_name_map.get(key, key)