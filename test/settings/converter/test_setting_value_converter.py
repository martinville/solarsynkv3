from unittest import TestCase

from src.settings.converter.setting_value_converter import SettingValueConverter

ANY_SETTING_NAME = 'any-setting-name'


class TestSettingValueConverter(TestCase):
    def setUp(self):
        self.setting_value_converter = SettingValueConverter({})

    def test_should_read_map_from_csv(self):
        setting_value_converter = SettingValueConverter()

        self.assertEqual('int', setting_value_converter.setting_value_map['safetyType'])

    def test_should_return_original_value_when_map_is_empty(self):
        self.setting_value_converter.setting_value_map = {}

        converted_value = self.setting_value_converter.convert_value(ANY_SETTING_NAME, 'the-setting-value')

        self.assertEqual(
            'the-setting-value',
            converted_value
        )

    def test_should_return_original_value_when_map_does_not_contain_setting_name(self):
        self.setting_value_converter.setting_value_map = {'the-setting-name': 'the-type'}

        converted_value = self.setting_value_converter.convert_value('the-other-setting-name', 'the-setting-value')

        self.assertEqual(
            'the-setting-value',
            converted_value
        )

    def test_should_return_original_value_when_map_contains_setting_name_but_no_conversion_available(self):
        self.setting_value_converter.setting_value_map = {'the-setting-name': 'the-type'}

        converted_value = self.setting_value_converter.convert_value('the-setting-name', 'the-setting-value')

        self.assertEqual(
            'the-setting-value',
            converted_value
        )

    def test_should_convert_t_to_true_for_boolean_setting_value(self):
        self.setting_value_converter.setting_value_map = {'the-setting-name': 'bool'}

        converted_value = self.setting_value_converter.convert_value('the-setting-name', 't')

        self.assertEqual('true', converted_value)

    def test_should_convert_f_to_false_for_boolean_setting_value(self):
        self.setting_value_converter.setting_value_map = {'the-setting-name': 'bool'}

        converted_value = self.setting_value_converter.convert_value('the-setting-name', 'f')

        self.assertEqual('false', converted_value)