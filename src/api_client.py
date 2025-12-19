import requests


def get_location(ip):
    url = f"https://freeipapi.com/api/json/{ip}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    # import ipdb; ipdb.set_trace()
    return {
        "ip": data.get("ipAddress"),
        "country": data.get("countryName"),
        "country_code": data.get("countryCode"),
        "region": data.get("regionName"),
        "city": data.get("cityName"),
        "latitude": data.get("latitude"),
        "longitude": data.get("longitude"),
        "timezone": data.get("timeZone"),
    }


if __name__ == "__main__":
    print(get_location("8.8.8.8"))
