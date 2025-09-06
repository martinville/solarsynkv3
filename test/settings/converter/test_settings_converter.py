from unittest import TestCase
from unittest.mock import MagicMock, call, patch

import src
from src.settings.converter.settings_converter import SettingsConverter


class TestSettingsConverter(TestCase):
    def setUp(self):
        self.setting_name_converter = MagicMock()
        self.setting_value_converter = MagicMock()

        package = src.settings.converter.settings_converter
        with patch.object(package, 'SettingNameConverter', return_value=self.setting_name_converter):
            with patch.object(package, 'SettingValueConverter', return_value=self.setting_value_converter):
                self.settings_converter = SettingsConverter()

    def test_convert_should_call_convert_settings_v2_to_v1_when_v2_prefix_is_present(self):
        self.settings_converter._convert_settings_v2_to_v1 = MagicMock()

        raw_settings = "v2#the-settings"

        self.settings_converter.convert(raw_settings)

        self.settings_converter._convert_settings_v2_to_v1.assert_called_once_with('the-settings')

    def test_convert_should_return_result_of_convert_settings_v2_to_v1_when_v2_prefix_is_present(self):
        self.settings_converter._convert_settings_v2_to_v1 = MagicMock(return_value='the-v1-settings')

        raw_settings = "v2#the-settings"

        converted_settings = self.settings_converter.convert(raw_settings)

        self.assertEqual(
            'the-v1-settings',
            converted_settings
        )

    def test_convert_should_not_call_convert_settings_v2_to_v1_when_v2_prefix_is_not_present(self):
        self.settings_converter._convert_settings_v2_to_v1 = MagicMock()

        raw_settings = "the-settings"

        self.settings_converter.convert(raw_settings)

        self.settings_converter._convert_settings_v2_to_v1.assert_not_called()

    def test_convert_should_return_original_settings_when_v2_prefix_is_not_present(self):
        raw_settings = "the-settings"

        converted_settings = self.settings_converter.convert(raw_settings)

        self.assertEqual(
            'the-settings',
            converted_settings
        )

    def test_convert_v2_to_v1_should_call_setting_name_converter_convert_name_for_each_setting_name(self):
        self.setting_name_converter.convert_name = MagicMock(return_value='the-converted-name')

        raw_settings = "the-setting-name:any-setting-value;the-other-setting-name:any-setting-value"

        self.settings_converter._convert_settings_v2_to_v1(raw_settings)

        self.setting_name_converter.convert_name.assert_has_calls(
            [
                call('the-setting-name'),
                call('the-other-setting-name')
            ]
        )

    def test_convert_v2_to_v1_should_call_setting_value_converter_convert_value_for_each_converted_setting_name_and_value(self):
        self.setting_name_converter.convert_name = MagicMock(side_effect=['the-converted-setting-name', 'the-other-converted-setting-name'])
        self.setting_value_converter.convert_value = MagicMock(return_value='the-converted-value')

        raw_settings = "the-setting-name:the-setting-value;the-other-setting-name:the-other-setting-value"

        self.settings_converter._convert_settings_v2_to_v1(raw_settings)

        self.setting_value_converter.convert_value.assert_has_calls(
            [
                call('the-converted-setting-name', 'the-setting-value'),
                call('the-other-converted-setting-name', 'the-other-setting-value')
            ]
        )

    def test_convert_v2_to_v1_should_return_settings_in_v1_format(self):
        self.setting_name_converter.convert_name = MagicMock(side_effect=['the-converted-setting-name', 'the-other-converted-setting-name'])
        self.setting_value_converter.convert_value = MagicMock(side_effect=['the-converted-setting-value', 'the-other-converted-setting-value'])

        raw_settings = "the-setting-name:the-setting-value;the-other-setting-name:the-other-setting-value"

        converted_settings = self.settings_converter._convert_settings_v2_to_v1(raw_settings)

        self.assertEqual(
            '"the-converted-setting-name":"the-converted-setting-value";"the-other-converted-setting-name":"the-other-converted-setting-value"',
            converted_settings
        )
