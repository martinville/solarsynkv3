from unittest import TestCase
from unittest.mock import MagicMock

from settings_converter import SettingsConverter


class TestSettingsConverter(TestCase):
    def setUp(self):
        self.settings_converter = SettingsConverter(
            {'tsn': 'the-setting-name'}
        )

    def test_convert_should_return_same_string_when_not_v2(self):
        self.settings_converter.v2_to_v1 = MagicMock()

        raw_settings = "the-settings"

        converted_settings = self.settings_converter.convert(raw_settings)

        self.assertEqual(
            'the-settings',
            converted_settings
        )

        self.settings_converter.v2_to_v1.assert_not_called()

    def test_convert_should_return_result_of_v2_to_v1_when_v2_prefix_is_present(self):
        self.settings_converter.v2_to_v1 = MagicMock(return_value='the-v1-settings')

        raw_settings = "v2#the-settings"

        converted_settings = self.settings_converter.convert(raw_settings)

        self.assertEqual(
            'the-v1-settings',
            converted_settings
        )

        self.settings_converter.v2_to_v1.assert_called_once_with('v2#the-settings')

    def test_v2_to_v1_should_strip_v2_prefix(self):
        raw_settings = "v2#"

        converted_settings = self.settings_converter.v2_to_v1(raw_settings)

        self.assertEqual(
            '',
            converted_settings
        )

    def test_v2_to_v1_should_leave_unmatched_names_as_is(self):
        raw_settings = "v2#a:b;c:d"

        converted_settings = self.settings_converter.v2_to_v1(raw_settings)

        self.assertEqual(
            '"a":"b";"c":"d"',
            converted_settings
        )

    def test_v2_to_v1_should_replace_matched_short_names_with_full_name(self):
        raw_settings = "v2#tsn:b;c:d"

        converted_settings = self.settings_converter.v2_to_v1(raw_settings)

        self.assertEqual(
            '"the-setting-name":"b";"c":"d"',
            converted_settings
        )


