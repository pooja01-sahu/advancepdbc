import pymysql

class DecorationBean():

    def __init__(self):
        self._DecorationId = 0
        self._Theme = ""
        self._VendorName = ""
        self._Cost = 0

    @property
    def DecorationId(self):
        return self._DecorationId

    @DecorationId.setter
    def DecorationId(self,value):
        self._DecorationId = value

    @property
    def Theme(self):
        return self._Theme

    @Theme.setter
    def Theme(self,value):
        self._Theme = value

    @property
    def VendorName(self):
        return self._VendorName

    @VendorName.setter
    def VendorName(self,value):
        self._VendorName = value

    @property
    def Cost(self):
        return self._Cost

    @Cost.setter
    def Cost(self,value):
        self._Cost = value
