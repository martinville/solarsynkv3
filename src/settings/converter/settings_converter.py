
from src.settings.converter.setting_name_converter import SettingNameConverter
from src.settings.converter.setting_value_converter import SettingValueConverter


class SettingsConverter:
    def __init__(self):
        self.setting_name_converter = SettingNameConverter()
        self.setting_type_converter = SettingValueConverter()

    def convert(self, raw_settings):
        # if the settings start with "v2#" then they'll need converting
        if raw_settings.startswith("v2#"):
            # strip the "v2#" prefix
            return self._convert_settings_v2_to_v1(raw_settings[3:])
        # otherwise, it's in the 'v1' format, so no conversion needed, just return as is
        return raw_settings

    def _convert_settings_v2_to_v1(self, raw_settings):
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
                full_key = self.setting_name_converter.convert_name(key)

                # convert the value to the correct type
                full_value = self.setting_type_converter.convert_value(full_key, value)

                v1_settings.append((full_key, full_value))

        # return the converted settings in the 'v1' format
        return ';'.join('"{}":"{}"'.format(key, value) for key, value in v1_settings)


if __name__ == "__main__":
    settings_converter = SettingsConverter()
    print(settings_converter.convert("v2#ge1:t;ge2:f"))
