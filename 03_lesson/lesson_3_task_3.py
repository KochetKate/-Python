from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Ленина", "10", "25")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "5", "13")

mailing_m = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=1000,
    track="TRACK123456789"
)

print(mailing_m)
