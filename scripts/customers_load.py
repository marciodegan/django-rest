import csv

from portfolio.models import Customers

def run():
    fhand = open('portfolio/customers.csv')
    reader = csv.reader(fhand)

    Customers.objects.all().delete()

    for row in reader:
        print(row)

        p, created = Customers.objects.get_or_create(id=row[0], first_name=row[1], last_name=row[2], email=row[3], gender=row[4], company=row[5], city=row[6], title=row[7])

