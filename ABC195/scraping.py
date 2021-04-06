import os
import requests

import bs4
from bs4 import BeautifulSoup

contest = __file__[18:-12].lower()
dirpath = __file__[:25] + 'testcase'


def scraping():
    contest_type = contest[:3] 
    contest_number = int(contest[3:])

    if (contest_type == 'abc' and 126 <= contest_number) or contest_type == 'agc' or (contest_type == 'arc' and 104 <= contest_number):
        difficulties = ['a', 'b', 'c', 'd', 'e', 'f']
    elif contest_type == 'arc' and 58 <= contest_number <= 103:
        difficulties = ['c', 'd', 'e', 'f']
    else:
        difficulties = ['a', 'b', 'c', 'd']

    for difficulty in difficulties:
        problem_url = "https://atcoder.jp/contests/" + contest + "/tasks/" + contest +  "_" + difficulty
        problem_html = requests.get(problem_url)
        problem_soup = BeautifulSoup(problem_html.content, "html.parser")
        testcase = []
        tags =  problem_soup.find_all("pre")
        for f in tags:
            testcase.append(f.get_text())

        n = len(testcase)//2
        if n%2:
            for i in range(1, n, 2):
                case_number = (i + 1) // 2

                in_path = dirpath + "/input_" + difficulty.upper() + str(case_number) + ".txt"
                f_in = open(in_path, "w")
                testcase[i] = testcase[i].replace('\n', '')
                f_in.write(testcase[i])
                f_in.close()

                out_path = dirpath + "/output_" + difficulty.upper() + str(case_number) + ".txt"
                f_out = open(out_path, "w")
                testcase[i+1] = testcase[i+1].replace('\n', '')
                f_out.write(testcase[i + 1])
                f_out.close()
        else:
            for i in range(2, n, 2):
                case_number = (i + 1) // 2

                in_path = dirpath + "/input_" + difficulty.upper() + str(case_number) + ".txt"
                f_in = open(in_path, "w")
                testcase[i] = testcase[i].replace('\n', '')
                f_in.write(testcase[i])
                f_in.close()

                out_path = dirpath + "/output_" + difficulty.upper() + str(case_number) + ".txt"
                f_out = open(out_path, "w")
                testcase[i+1] = testcase[i+1].replace('\n', '')
                f_out.write(testcase[i + 1])
                f_out.close()
    return