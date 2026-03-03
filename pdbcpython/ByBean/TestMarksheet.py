from MarksheetModel import MarksheetModel
from MarksheetBean import MarksheetBean


def testadd():
    mark = MarksheetBean()
    mark.rollno = 25
    mark.name = "Janki"
    mark.physics = 85
    mark.chemistry = 65
    mark.maths = 85
    model = MarksheetModel()
    model.add(mark)


def testGet():
    model = MarksheetModel()
    list = model.get(1)
    for data in list:
        print(data['id'], '\t', data['rollno'], '\t', data['name'], '\t', data['physics'], '\t', data['chemistry'],
              '\t',
              data['maths'], )


def testupdate():
    mark = MarksheetBean()

    mark.id = 3
    mark.rollno = 35
    mark.name = 'Janki'
    mark.physics = 70
    mark.chemistry = 67
    mark.maths = 79

    model = MarksheetModel()
    model.update(mark)


def testDelete():
    model = MarksheetModel()
    model.delete(2)


# testadd()
# testGet()
# testupdate()
testDelete()
