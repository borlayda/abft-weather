#!/usr/bin/env python

from requests import get
from matrix import *

HOST_URL = "https://totlol.me/temp"

def get_weekly_data():
    data = get(HOST_URL)
    matrices = data.json()["matrices"]
    checksums = data.json()["sum"]
    summ_matrix, c_check, r_check = make_summ(matrices)
    print_matrix(summ_matrix)
    iterate_matrix(checksums, r_check, c_check)
    print_matrix(checksums)

if __name__ == '__main__':
    get_weekly_data()
