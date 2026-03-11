import pymysql

class DonationCampBean():

    def __init__(self):
        self._campId = 0
        self._campName = ""
        self._campDate = None
        self._organizer = ""

    @property
    def campId(self):
        return self._campId

    @campId.setter
    def campId(self, value):
        self._campId = value

    @property
    def campName(self):
        return self._campName

    @campName.setter
    def campName(self, value):
        self._campName = value

    @property
    def campDate(self):
        return self._campDate

    @campDate.setter
    def campDate(self, value):
        self._campDate = value

    @property
    def organizer(self):
        return self._organizer

    @organizer.setter
    def organizer(self, value):
        self._organizer = value
