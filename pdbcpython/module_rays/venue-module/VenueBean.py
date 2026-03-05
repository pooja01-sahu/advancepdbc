import pymysql

class VenueBean():

    def __init__(self):
        self._venueId = 0
        self._venueName = ""
        self._city = ""
        self._capital = ""

    @property
    def venueId(self):
        return self._venueId

    @venueId.setter
    def venueId(self, value):
        self._venueId = value

    @property
    def venueName(self):
        return self._venueName

    @venueName.setter
    def venueName(self, value):
        self._venueName = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def capital(self):
        return self._capital

    @capital.setter
    def capital(self, value):
        self._capital = value
