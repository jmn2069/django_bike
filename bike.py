class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        print self.price
        print self.max_speed
        print self.miles

    def ride(self):
        print "Riding..."
        self.miles += 10
        return self

    def reverse(self):
        if self.miles > 0:
            print "Reversing..."
            self.miles -= 5
        else:
            print "Cannot reverse, bike doesn't have enough miles."
        return self
    
bike1 = Bike(100, "25mph")
bike2 = Bike(200, "35mph")
bike3 = Bike(500, "55mph")

bike1.ride().ride().ride().reverse()
bike1.displayinfo()

bike2.ride().ride().reverse().reverse()
bike2.displayinfo()

bike3.reverse().reverse().reverse()
bike3.displayinfo()


