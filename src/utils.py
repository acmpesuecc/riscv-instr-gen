#
#  Utils for RIG
#

# ------- Imports -------
import os
import sys
import re

# ------- Classes -------
class RV_instruction_generator:
    # init func
    def __init__(self, isa):
        self.isa = isa

    # ISA match
    def isa_format_check(self):
        list_bit_width = [32, 64]    # List of allowed bit widths
        list_extension = ["I"]       # List of allowed extensions
        
        # regex check to confine with the ISA format
        for bw in list_bit_width:
            match = re.search(f"RV+{bw}", self.isa)
            if match:
                error_flag = False
                break
            else:
                error_flag = True
        if error_flag:
            print("Enter valid ISA Extension!")

        # check extensions
        isa_ext = list(self.isa)[4:]

        # check extensions with allowed list
        for ext in isa_ext:
            if ext in list_extension:
                error_flag = False
            else:
                error_flag = True
        if error_flag:
            print("Enter valid ISA Extension!")

isa_test = "RV32I"
r1 = RV_instruction_generator(isa_test)
r1.isa_format_check()
