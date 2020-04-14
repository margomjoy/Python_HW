import os
import csv

cereal_csv = os.path.join("../Resources 1.1", "cereal.csv")

with open(cereal_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    skip= next(csvreader, None)
    print("The cereals that contain 5g of fiber or more")
    for row in csvreader:
        name=row[0]
        fiber=float(row[7])
        if fiber>=5:
            print('{:50s} {:.1f}'.format(name,fiber))
            