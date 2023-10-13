#======================================================
#	RISC-V Instruction Generator
#	Testing your cores, sims and ems made simpler!
#======================================================

# Imports
import os
import click
import sys

# CLI

import argparse
from utils import RV_instruction_generator

parser = argparse.ArgumentParser(description="RISC-V Instruction Generator CLI")
parser.add_argument("--generate", action="store_true", help="Generate RISC-V instructions")
parser.add_argument("--isa", help="Specify the ISA format (e.g., RV32I)")

args = parser.parse_args()

if args.generate:
    if args.isa:
        r1 = RV_instruction_generator(args.isa)
        r1.isa_format_check()
        r1.instr_gen()
    else:
        print("Please specify the ISA format using --isa.")

if __name__ == "__main__":
    args = parser.parse_args()

    if args.generate:
        if args.isa:
            r1 = RV_instruction_generator(args.isa)
            r1.isa_format_check()
            r1.instr_gen()
        else:
            print("Please specify the ISA format using --isa.")
