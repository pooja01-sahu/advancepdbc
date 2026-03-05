from VenueModule import VenueModel
from VenueBean import VenueBean


def testadd():
    ven = VenueBean()
    ven.venueId = 5
    ven.venueName = 'Sports Complex'
    ven.city = 'Mumbai'
    ven.capital = "Maharashtra"
    model = VenueModel()
    model.add(ven)

def testGet():
    ven = VenueModel()
    list = ven.get(2)
    for data in list:
        print(data['venueId'], '\t', data['venueName'], '\t', data['city'], '\t', data['capital'])

def testupdate():
    ven = VenueBean()
    ven.venueId = 4
    ven.venueName = 'Grand Palace Hall'
    ven.city = 'Hyderabad'
    ven.capital = "Telangana"
    model = VenueModel()
    model.update(ven)


def testDelete():
    model = VenueModel()
    model.delete(6)

# testadd()
# testGet()
# testupdate()
testDelete()