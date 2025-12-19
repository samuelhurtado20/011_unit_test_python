from src.api_client import get_location
import unittest
import requests
import json
from unittest.mock import patch


class ApiClientTests(unittest.TestCase):

    @patch("src.api_client.requests.get")
    def test_get_location_success(self, mock_get):
        mock_get.return_value.json.return_value = {"countryName": "United States"}
        location = get_location("8.8.8.8")
        self.assertEqual(location.get("country"), "United States")

    @patch("src.api_client.requests.get")
    def test_get_location_failure(self, mock_get):
        mock_get.return_value.json.return_value = {"countryName": "Colombia"}
        location = get_location("8.8.8.8")
        self.assertNotEqual(location.get("country"), "Usa")
        
        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")


    @patch('src.api_client.requests.get')
    def test_get_location_returns_full_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "ipAddress": "8.8.8.8",
            "countryName": "USA",
            "countryCode": "US",
            "regionName": "FLORIDA",
            "cityName": "MIAMI",
            "latitude": 25.7617,
            "longitude": -80.1918,
            "timeZone": "America/New_York"
        }

        result = get_location("8.8.8.8")

        self.assertEqual(result["ip"], "8.8.8.8")
        self.assertEqual(result["country"], "USA")
        self.assertEqual(result["country_code"], "US")
        self.assertEqual(result["region"], "FLORIDA")
        self.assertEqual(result["city"], "MIAMI")
        self.assertEqual(result["latitude"], 25.7617)
        self.assertEqual(result["longitude"], -80.1918)
        self.assertEqual(result["timezone"], "America/New_York")

        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")