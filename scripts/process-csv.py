# process_csv.py
# using file with dates from 1990 to 2017
# data from ourworldindata.org/internet

import csv
import sys

def process():
    filename = 'number-of-internet-users-by-country'
    input_csv = filename + '.csv'

    start_date = 1990
    end_date = 2017
    date_range = end_date - start_date
    def toYear(y):
        return y + start_date

    d = {}
    name_i = 0
    year_i = 2
    val_i = 3

    # read in csv file
    with open(input_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        n = 0

        for row in csv_reader:
            if n==0:
                print(row)
                n += 1
            else:
                name = row[name_i]
                year = row[year_i]
                val = row[val_i]

                if (name in d):
                    #d.update([(name, d[name] + [[year,val]])])
                    #d.update([(name, d[name] + [val])])
                    tmp = d[name]
                    i = int(year) - start_date
                    tmp[i] = val
                    d.update([(name, tmp)])
                else:
                    #d.update([(name, [[year,val]])])
                    #d.update([(name, [val])])
                    d.update([(name, ['0'] * (date_range + 1))])

        # get rid of gaps in data, use most recent available data
        # use w caution, can be misleading
        for k in d.keys():
            arr = d[k]
            for i in range(1,len(arr)-1):
                if arr[i] == "0":
                    arr[i] = arr[i-1]
                d.update([(k, arr)])

    # write to csv output
    with open(filename + '-transposed.csv', 'w') as outfile:
        writer = csv.writer(outfile, delimiter=',', quotechar='"')
        names = d.keys()
        b = 0

        s = 'writer.writerow(["Name",'
        for y in range(0, date_range-1):
            s += '"' + str(y + start_date) + '",'
        s += '"' + str(end_date) + '"])'
        print(s)
        exec(s)

        for name in names:
            s = 'writer.writerow('
            s += '["' + name + '","' 
            s += '","'.join(map(str, d[name])) + '"]'
            s += ')'
            exec(s)
            
            if (b == 0):
                print(s)
            b += 1
            #writer.writerow([name, d[name][0]])

process()
print("done")
