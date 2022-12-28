from datetime import datetime
NOW = datetime.now()


class Promo:
    def __init__(self, name, expires):
        self.name = name
        self.expires = expires

    def _expiredCheck(self):
        return self.expires < datetime.now()
    
    expired = property(fget=_expiredCheck)