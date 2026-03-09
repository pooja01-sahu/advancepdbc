from module_rays.Decoration.DecorationBean import DecorationBean
from module_rays.Decoration.DecorationModule import DecorationModule


def testadd():
    dec = DecorationBean()
    dec.DecorationId = 4
    dec.Theme = "Beach Theme"
    dec.VendorName = "Dream Planner"
    dec.Cost = 900000
    model = DecorationModule()
    model.add(dec)

def testget():
    model = DecorationModule()
    list = model.get(2)
    for data in list:
        print(data['decorationId'], '\t', data['theme'], '\t',data["vendorName"],'\t',data['cost'])

def testupdate():
    dec = DecorationBean
    dec.DecorationId = 4
    dec.Theme = "Royal wedding"
    dec.VendorName = "shree Decorator"
    dec.Cost = 3000000
    model = DecorationModule()
    model.update(dec)
    print("data updated successfully")

def testDelete():
    model = DecorationModule()
    model.delete(2)




testDelete()
# testadd()
# testget()
# testupdate()