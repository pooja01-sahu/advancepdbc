import pymysql
from DonationCampBean import DonationCampBean
from DonationCampModule import DonationCampModule

class DonationCampTest():

    def testAdd(self):
        camp = DonationCampBean
        camp.campId = 1
        camp.campName = "Health Camp"
        camp.campDate = '2026-03-05'
        camp.organizer = "Red Cross"
        model = DonationCampModule
        model.add(camp)


