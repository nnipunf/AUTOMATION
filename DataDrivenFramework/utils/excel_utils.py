import openpyexcel

def get_row_count(file, sheet):
    workbook = openpyexcel.load_workbook(file)
    worksheet = workbook.get_sheet_by_name(sheet)
    return worksheet.max_row