# !/usr/bin/env python
# -*- coding: shift-jis -*-

import os
import subprocess

from scraping import scraping

TLE = 2.0
problem = os.environ["problem"]
contest = os.environ["contest"]
dirpath = contest + "\\testcase"


def main():
    # make a directory of testcases
    if not os.path.exists(dirpath): 
        os.makedirs(dirpath)
        scraping()

    number_of_probrems = 0
    for number in range(1, 100):
        if os.path.isfile(dirpath + "/input_" + problem + str(number) + ".txt"):
            number_of_probrems += 1
        else:
            break

    is_correct = True
    for number in range(1, number_of_probrems + 1):  # number of testcases
        in_path = dirpath + "/input_" + problem + str(number) + ".txt"
        out_path = dirpath + "/output_" + problem + str(number) + ".txt"
        res_path = dirpath + "/response_" + problem + str(number) + ".txt"

        # execute the program
        f = open(in_path)
        data = f.read()
        f.close()
        with open(in_path) as fin:
            with open(res_path, "w") as fres:
                subprocess.run("python " + contest + "\\" + problem + ".py", stdin=fin, stdout=fres, timeout=TLE, shell = True)

        # check the response
        f_out = open(out_path, "r")
        out_str = "".join(f_out.read().splitlines())
        f_out.close()

        f_res = open(res_path, "r")
        res_str = "".join(f_res.read().splitlines())
        f_res.close()

        if out_str != res_str:
            is_correct = False
            print("Sample " + str(number) + " WA")
        else:
            print("Sample " + str(number) + " AC")

    # output the result
    if is_correct:
        print("Sample OK!")
    else:
        print("Wrong Answer exist.")
    return


if __name__ == "__main__":
    main()
