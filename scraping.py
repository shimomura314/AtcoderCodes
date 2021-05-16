import os
import requests

import bs4
from bs4 import BeautifulSoup

problem = os.environ["problem"]
file_path = os.environ["contest"]
dirpath = file_path + "\\testcase"
contest = file_path[-6:].lower()

def scraping():
    contest_type = contest[:3] 
    contest_number = int(contest[3:])

    if (contest_type == "abc" and 126 <= contest_number) or contest_type == "agc" or (contest_type == "arc" and 104 <= contest_number):
        difficulties = ["a", "b", "c", "d", "e", "f"]
    else:
        difficulties = ["a", "b", "c", "d"]
    
    mixed_ABC_number = [
        102, 101, 98, 97, 95, 94, 93, 92, 91, 90, 
        87, 86, 83, 82, 81, 78, 77, 74, 73, 71, 
        69, 68, 67, 66, 65, 63, 62, 60, 59, 58, 
        56, 55, 53, 52, 50, 49, 48, 47, 46, 45, 
        44, 43, 42
        ]
    mixed_ABC = {}
    for i in range(len(mixed_ABC_number)):
        mixed_ABC[ mixed_ABC_number[i] ] = "arc%03d" %(100-i)

    for difficulty in difficulties:
        if contest_type == "abc" and (contest_number in mixed_ABC_number) and (difficulty == "c" or difficulty == "d"):
            if difficulty == "c":
                problem_url = "https://atcoder.jp/contests/" + contest + "/tasks/" + mixed_ABC[contest_number] +  "_a"
            if difficulty == "d":
                problem_url = "https://atcoder.jp/contests/" + contest + "/tasks/" + mixed_ABC[contest_number] +  "_b"
        else:
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
                testcase[i] = testcase[i].replace("\n", "")
                f_in.write(testcase[i])
                f_in.close()

                out_path = dirpath + "/output_" + difficulty.upper() + str(case_number) + ".txt"
                f_out = open(out_path, "w")
                testcase[i+1] = testcase[i+1].replace("\n", "")
                f_out.write(testcase[i + 1])
                f_out.close()
        else:
            for i in range(2, n, 2):
                case_number = (i + 1) // 2

                in_path = dirpath + "/input_" + difficulty.upper() + str(case_number) + ".txt"
                f_in = open(in_path, "w")
                testcase[i] = testcase[i].replace("\n", "")
                f_in.write(testcase[i])
                f_in.close()

                out_path = dirpath + "/output_" + difficulty.upper() + str(case_number) + ".txt"
                f_out = open(out_path, "w")
                testcase[i+1] = testcase[i+1].replace("\n", "")
                f_out.write(testcase[i + 1])
                f_out.close()
    return