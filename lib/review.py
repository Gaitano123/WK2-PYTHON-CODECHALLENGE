class Review:
    
    all = []
    
    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review.all.append(self)
        # customer.add_review(self)
        
    def rating(self):
        return self._rating
          
    @classmethod
    def all(cls):
        return cls.all
    
    def customer(self):
        return self._customer
    
    def restaurant(self):
        return self._restaurant
    