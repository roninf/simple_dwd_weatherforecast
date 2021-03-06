import unittest
from simple_dwd_weatherforecast import dwdforecast


class StationTestCase(unittest.TestCase):
    def test_get_nearest_station_id(self):
        self.assertEqual(
            dwdforecast.get_nearest_station_id(50.272388, 8.645408),
            "L732",
            "Wrong nearest station",
        )

    def test_is_valid_station_id_true(self):
        self.assertTrue(dwdforecast.is_valid_station_id("EW024"))
        self.assertTrue(dwdforecast.is_valid_station_id("17600"))
        self.assertTrue(dwdforecast.is_valid_station_id("H889"))
        self.assertTrue(dwdforecast.is_valid_station_id("F9509"))
        self.assertTrue(dwdforecast.is_valid_station_id("X228"))
        self.assertTrue(dwdforecast.is_valid_station_id("57083"))
        self.assertTrue(dwdforecast.is_valid_station_id("W4835"))

    def test_is_valid_station_id_false(self):
        self.assertFalse(dwdforecast.is_valid_station_id("EWd024"))
        self.assertFalse(dwdforecast.is_valid_station_id("&$%"))

    def test_is_valid_station_id_empty_string(self):
        self.assertFalse(dwdforecast.is_valid_station_id(""))
        self.assertFalse(dwdforecast.is_valid_station_id(1))
