from model.contact import Contact

#import random
#import string

testdata = [
    Contact(lastname="name21", firstname="name12", home_phone="123-7", email2="mail@google.ru"),
    Contact(firstname="name1aaa", lastname="name22aaa", work_phone="765-123", email="mail@google.ru", email3="mail@google.ru")
]


#def random_name(prefix, maxlen):
#    symbols = string.ascii_letters + " "
#    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


#def random_phone(maxlen):
#    symbols = string.digits * 5 + string.punctuation
#    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


#testdata = [Contact(lastname="", firstname="", email="", home_phone="")] + [
#    Contact(firstname=random_name("Fname", 10), lastname=random_name("Lname", 14), email=random_name("email", 18), home_phone=random_phone(10), email2=random_name("email", 18), work_phone=random_phone(10))
#    for i in range(10)
#]
