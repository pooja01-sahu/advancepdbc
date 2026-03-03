class MarksheetBean():

    def __init__(self):
        self.__id = 0
        self.__rollno = 0
        self.__name = ""
        self.__physics = 0
        self.__chemistry = 0
        self.__maths = 0

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,id):
        self.__id = id

    @property
    def roll_no(self):
        return self.__rollno

    @roll_no.setter
    def roll_no(self, rollno):
        self.__rollno = rollno

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def physics(self):
        return self.__physics

    @physics.setter
    def physics(self, physics):
        self.__physics = physics

    @property
    def chemistry(self):
        return self.__chemistry

    @chemistry.setter
    def chemistry(self, chemistry):
        self.__chemistry = chemistry

    @property
    def maths(self):
        return self.__maths

    @maths.setter
    def maths(self, maths):
        self.__maths = maths
