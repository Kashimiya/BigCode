import os
import csv


class TimeZoneHandler:
    after_pca_path = ""

    def __init__(self):
        self.after_pca_path = os.path.abspath('..\\..') + '\\doc\\after_pca.csv'

    def TimeZonePrint(self):
        res = ""
        for i in range(0, 24):
            with open(self.after_pca_path, 'r') as f:
                reader = csv.reader(f)
                average = 0.0
                count = 0
                for row in reader:
                    if int(row[0]) == i:
                        count += 1
                        average = (average + float(row[1])) / count
                if (count <= 5):
                    average = 0.0
                res += str(i) + "," + str(average) + "," + str(count) + "\n"

        tbt_path = os.path.abspath('..\\..') + '\\doc\\typed_by_time.csv'
        doc = open(tbt_path, 'w')

        doc.write(res)
        doc.close()


if __name__ == '__main__':
    tzh = TimeZoneHandler()
    print(tzh.after_pca_path)
    tzh.TimeZonePrint()
