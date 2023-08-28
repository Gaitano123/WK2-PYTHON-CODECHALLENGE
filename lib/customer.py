from review import Review

class Customer:
    
    group = []
    
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        Customer.group.append(self)
        
    @property
    def given_name(self):
        return self._first_name
    
    @property
    def family_name(self):
        return self._last_name
    
    @family_name.setter
    def family_name(self, value):
        self._last_name = value
 
    def full_name(self):
        return f'{self._first_name} {self._last_name}'    
    
    @classmethod
    def all(cls):
        return cls.group
    
    def restaurant(self):
        return list({ review for review in Review.all if review.customer.full_name == self.full_name })
    
    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.review.append(review)
    
    def num_reviews(self):
        return len([ review for review in Review if review.customer.full_name == self.full_name])
    
    def find_by_name(full_name):
        for customer in Customer.group:
            if customer.full_name == full_name:
                return customer
            
    def find_all_by_given_name(name):
        search = []
        for customer in Customer.group:
            if customer.given_name == name:
                search.append(customer) 
        return search     

customer1 = Customer('Gaitano', 'George')

print(customer1.full_name())

