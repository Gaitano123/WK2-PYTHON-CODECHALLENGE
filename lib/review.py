class Review:
    
    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        
    def rating(self):
        return self._rating
    
    def set_rating(self, value):
        if type(value) == int:
            if 0<= value <= 5:
                self._rating = value
            else:
                print("Rating should be between 0 and 5")
        else:
            print("Rating should be a number between 0 and 5")
    
    pass