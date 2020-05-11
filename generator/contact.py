from model.contact import Contact

import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_name(prefix, maxlen):
    symbols = string.ascii_letters + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    symbols = string.digits * 5 + string.punctuation
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(lastname="", firstname="", email="", home_phone="")] + [
    Contact(firstname=random_name("Fname", 10), lastname=random_name("Lname", 14), email=random_name("email", 18),
            home_phone=random_phone(10), email2=random_name("email", 18), work_phone=random_phone(10), phone2=random_phone(10))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as file_out:
    jsonpickle.set_encoder_options("json", indent=2)
    file_out.write(jsonpickle.encode(testdata))
