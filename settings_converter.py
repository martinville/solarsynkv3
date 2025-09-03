from csv import DictReader


class SettingsConverter:
    def __init__(self, setting_name_map=None):
        if setting_name_map is None:
            setting_name_map = {}
            setting_type_map = {}

            with open('setting_names.csv', 'r') as reader:
                dict_reader = DictReader(reader)

                for row in dict_reader:
                    setting_name = row['name']
                    setting_name_map[row['short_name']] = setting_name
                    setting_type_map[setting_name] = row['type']

        self.v2_short_setting_name_map = setting_name_map

    def convert(self, raw_settings):
        # if the settings start with "v2#" then they'll need converting
        if raw_settings.startswith("v2#"):
            return self.v2_to_v1(raw_settings)
        # otherwise, it's in the 'v1' format, so no conversion needed, just return as is
        return raw_settings

    def v2_to_v1(self, raw_settings):
        # strip the "v2#" prefix
        raw_settings = raw_settings[3:]

        # split out the setting pairs
        setting_pairs = raw_settings.split(';')

        v1_settings = []

        # loop through the pairs
        for pair in setting_pairs:
            # ignore empty pairs
            if pair != '':
                # convert the pair to a key/value pair
                key, value = pair.split(':')

                # convert the short name to the full name
                full_key = self.v2_short_setting_name_map.get(key, key)

                v1_settings.append((full_key, value))

        # return the converted settings in the 'v1' format
        return ';'.join('"{}":"{}"'.format(key, value) for key, value in v1_settings)






