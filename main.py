import requests as req
import json


class Fake_Me():
    def __init__(self) -> None:
        pass

    def Rand_Address() -> object:
        '''Returns a randomized, Fake_Address object.'''
        jaddr = json.loads(
            req.get("https://fakerapi.it/api/v1/addresses?_quantity=1").text)
        data = jaddr["data"][0]

        return Fake_Address(data["street"], data["city"], data["country"], data["zipcode"], data["county_code"], str(data["latitude"]), str(data["longitude"]))


class Fake_Address():
    def __init__(self, street, city, country, zipcode, county_code, latitude, longitude) -> None:
        self.Street = street
        self.City = city
        self.Zipcode = zipcode
        self.Country = country
        self.County_Code = county_code
        self.Latitude = latitude
        self.Longitude = longitude
        self.Lat_And_Long = f"{latitude}, {longitude}"
        self.Full = f"{street}, {city}, {country}, {zipcode}"


if __name__ == "__main__":
    rnd_address = Fake_Me.Rand_Address()
    print(rnd_address.Full)
