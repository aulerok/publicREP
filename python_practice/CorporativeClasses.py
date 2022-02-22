class Guest:
    def __init__(self, fullname, city, status,):
        self.fullname = fullname
        self.city = city
        self.status = status

    def guest_info(self):
        return self.fullname

    def guest_status(self):
        return self.status

    def guest_city(self):
        return self.city
