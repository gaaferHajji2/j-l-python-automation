from openpyxl import load_workbook

workbook = load_workbook('jloka_test_01.xlsx');

print("Sheet Names Are: ", str(workbook.sheetnames));

sheet = workbook.active

print("The Value of A1 cell: ", sheet['A1'].value);

print("The Cell Value is: ", sheet.cell(row=1, column=1).value)

workbook.close();