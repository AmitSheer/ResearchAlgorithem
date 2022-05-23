import gspread
import numpy as np


def generate_matrix(sheet: gspread.worksheet.Worksheet):
    matrix = []
    for row in sheet.get_all_values():
        matrix.append([int(x) for x in row])
    return np.array(matrix)


def matmul():
    account = gspread.service_account('lecture-to-manuscript-5d87edd594cd.json')
    spsheet = account.open('research')
    A = spsheet.worksheet('A')
    B = spsheet.worksheet('B')
    cell = A.acell('A5')
    A_mat = generate_matrix(A)
    B_mat = generate_matrix(B)
    result_mat = np.matmul(A_mat, B_mat)
    try:
        result_sheet = spsheet.worksheet('A_times_B')
    except:
        result_sheet = spsheet.add_worksheet('A_times_B', result_mat.shape[0], result_mat.shape[1])
    result_sheet.update(result_mat.tolist())


if __name__ == '__main__':
    matmul()
