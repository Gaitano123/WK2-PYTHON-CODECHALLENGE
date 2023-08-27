class Customer:
    
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
    
    @property    
    def given_name(self):
        return self._first_name
    
    @given_name.setter
    def given_name(self, first_name):
        self._first_name = first_name
    
    @property    
    def family_name(self):
        return self._family_name
    
    @family_name.setter
    def family_name(self, last_name):
        self._last_name = last_name
        
    def full_name(self):
        return f'{self._first_name} {self._last_name}'    
            
    pass

name = Customer('Gaitano', 'George')

print(name.given_name)

