from collections import namedtuple

Address = namedtuple('Address', ['street', 'city', 'country'])

house = Address('221B Baker Street','London','England')