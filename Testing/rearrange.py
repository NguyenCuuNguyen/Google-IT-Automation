#!/usr/bin/env python3

import re

def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result is None:
        return name #if name == "", return "". If name == 1 word, return 1 word
    print("result[0] is {}".format(result[0]))
    return "{} {}".format(result[2], result[1])
