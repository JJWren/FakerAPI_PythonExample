import requests as req
import json


class FakeMe():
    def __init__(self) -> None:
        pass

    def Rand_Address() -> object:
        '''Returns a randomized, Fake_Address object.'''
        jaddr = json.loads(
            req.get("https://fakerapi.it/api/v1/addresses?_quantity=1").text)
        data = jaddr["data"][0]

        return FakeAddress(data["street"], data["city"], data["country"], data["zipcode"], data["county_code"], str(data["latitude"]), str(data["longitude"]))


class FakeAddress():
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
    print(f"10 Random Fake Addresses:")
    num = 10
    while num > 0:
        # The more efficient route would be to make a method that sets quantity called from the API to 10 or to use user input to select how many should be generated. These could be stored in a list or set and printed back. This would reduce calls to the API and be a faster implementation.
        print(FakeMe.Rand_Address().Full)
        num -= 1
