from unittest import TestCase

from src.settings.converter.setting_name_converter import SettingNameConverter


class TestSettingNameConverter(TestCase):
    def setUp(self):
        self.setting_name_converter = SettingNameConverter({})

    def test_should_read_map_from_csv(self):
        setting_name_converter = SettingNameConverter()

        self.assertEqual('safetyType', setting_name_converter.setting_name_map['st'])

    def test_should_return_original_name_when_csv_is_empty(self):
        self.setting_name_converter.setting_name_map = {}

        converted_name = self.setting_name_converter.convert_name('the-setting-name')

        self.assertEqual(
            'the-setting-name',
            converted_name
        )

    def test_should_return_original_name_when_name_is_not_in_csv(self):
        self.setting_name_converter.setting_name_map = {'the-setting-name': 'the-converted-setting-name'}

        converted_name = self.setting_name_converter.convert_name('the-other-setting-name')

        self.assertEqual(
            'the-other-setting-name',
            converted_name
        )

    def test_should_return_converted_name_when_name_is_in_csv(self):
        self.setting_name_converter.setting_name_map = {'the-setting-name': 'the-converted-setting-name'}

        converted_name = self.setting_name_converter.convert_name('the-setting-name')

        self.assertEqual(
            'the-converted-setting-name',
            converted_name
        )


