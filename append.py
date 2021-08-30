#!/usr/bin/env python3
# Copyright 2021 Erfan Abdi
# SPDX-License-Identifier: GPL-3.0-or-later

import json
import argparse

# Instantiate the parser
parser = argparse.ArgumentParser(description='OTA JSON Data appender')

# Required positional argument
parser.add_argument('JSON_FILE')
parser.add_argument('TIMESTAMP')
parser.add_argument('ZIP_NAME')
parser.add_argument('ZIP_SHA')
parser.add_argument('BUILD_TYPE')
parser.add_argument('ZIP_SIZE')
parser.add_argument('ZIP_URL')
parser.add_argument('ROM_VERSION')
args = parser.parse_args()

new_ota = {
            "datetime": int(args.TIMESTAMP),
            "filename": args.ZIP_NAME,
            "id": args.ZIP_SHA,
            "romtype": args.BUILD_TYPE,
            "size": int(args.ZIP_SIZE),
            "url": args.ZIP_URL,
            "version": args.ROM_VERSION
        }

with open(args.JSON_FILE, 'r+') as file:
    file_data = json.load(file)
    file_data["response"].insert(0, new_ota)
    file.seek(0)
    json.dump(file_data, file, indent=4)

print("Done")
