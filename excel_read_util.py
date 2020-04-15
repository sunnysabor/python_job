import xlrd

file = '/Users/jerry/Downloads/佛山.xlsx'


def read_excel(file):
    wb = xlrd.open_workbook(filename=file)
    sheets = wb.sheet_names()
    sheet1 = wb.sheet_by_index(0)

    try:
        sheet2 = wb.sheet_by_name('')  # 通过sheet名字获取表格
    except:
        print("根据名称获取sheet失败")
    rows = sheet1.row_values(2)  # 获取行内容
    cols = sheet1.col_values(3)  # 获取列内容
    # 获取单元格内容
    cels = sheet1.cell(1, 0).value
    cels2 = sheet1.cell_value(1, 0)
    cels3 = sheet1.row(1)[0].value


def readByRow(file):
    excel = xlrd.open_workbook(file)
    worksheet = excel.sheet_by_index(0)
    row = worksheet.nrows
    for i in range(row):
        row_data = worksheet.row_values(i)  # i行的list
        # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
        # Python 2.3. 以上版本可用，2.6 添加 start 参数。
        for a, b in enumerate(row_data):
            # i表示行数 a表示列数 b表示数据本身
            print(i, a, b)


# read_excel(file)
readByRow(file)
