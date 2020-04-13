from sys import maxsize

class Contact:
    def __init__(self, id=None, firstname=None, middlename=None, lastname=None, company=None, address=None, home_phone=None, mobile_phone=None, work_phone=None, fax=None, email=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.lastname == other.lastname) and (self.firstname == other.firstname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
