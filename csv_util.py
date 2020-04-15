import csv

file = '/Users/jerry/Downloads/行业mcc.csv';


##获取某一行
def getFileLineByNum(index, file):
    with open(file, 'r', encoding='gbk') as f:
        reader = csv.reader(f)
        list_result = list(reader)
        print(list_result[index])


##读写csv
def readAndWrite(file):
    with open(file, 'r', encoding='gbk') as s:
        with open('temp.csv', 'w') as t:
            source = csv.reader(s)
            target = csv.writer(t)
            for row in source:
                tmp1 = row[0] + row[1]
                row.append(tmp1)
                target.writerow(row)
        source.close()
        target.close()


readAndWrite(file)

#
# with open(file, 'r', encoding='gbk') as f:
#     reader = csv.reader(f)
#     print(type(reader))
#
#     for row in reader:
#         var0 = row[0]
#         var1 = row[1]
#         var2 = row[2]
