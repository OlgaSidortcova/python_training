from sys import maxsize

class Contact:
    def __init__(self, id=None, firstname=None, middlename=None, lastname=None, company=None, address=None,
                 home_phone=None, mobile_phone=None, work_phone=None, all_phone_from_home_page=None, fax=None,
                 email2=None, email3=None, email=None, all_emails_from_home_page=None, phone2=None):
        self.id = id
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
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_phone_from_home_page = all_phone_from_home_page
        self.phone2 = phone2


    def __repr__(self):
        return "%s:%s:%s:%s:%s" % (self.id, self.lastname, self.firstname, self.email, self.home_phone)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.lastname == other.lastname) and \
               (self.firstname == other.firstname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
