class HotelRoomCalc(object):
    'Hotel room rate calculator'

    def __init__(self, rt, sales=0.085, rm=0.1):
        '''HotelRoomCalc default arguments:
        sales tax == 8.5% and room tax == 10%'''
        self.salesTax = sales
        self.roomTax = rm
        self.roomRate = rt

    def calcTotal(self, days=1):
        'Calculate total; default to daily rate'
        daily = round((self.roomRate * (1 + self.roomTax + self.salesTax)), 2)
        return float(days) * daily

# San Francisco
sfo = HotelRoomCalc(299) # new instance
print sfo.calcTotal() # daily rate
print sfo.calcTotal(2) # 2-day rate

# Seattle
sea = HotelRoomCalc(189, 0.086, 0.058) # new instance
print sea.calcTotal()
print sea.calcTotal(4)

# Washington.D.C
wasWkDay = HotelRoomCalc(169, 0.045, 0.02) # new instance
wasWkEnd = HotelRoomCalc(119, 0.045, 0.02) # new instance
print wasWkDay.calcTotal(5) + wasWkEnd.calcTotal() # 7-day rate
