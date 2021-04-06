# !/usr/bin/env python
# -*- coding: shift-jis -*-

import glob
import os
import shutil

top_path = "c:\m\AtcoderCodes"


def main():
    folders = [folder for folder in os.listdir(top_path) if os.path.isdir(os.path.join(top_path, folder))]
    print(folders)
    for folder in folders:
        if folder == ".vscode" or folder == "template":
            continue
        shutil.copy('./template/pretest.py', top_path + "/" + folder)
        shutil.copy('./template/scraping.py', top_path + "/" + folder)


if __name__ == "__main__":
    main()