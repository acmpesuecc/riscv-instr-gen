#======================================================
#	RISC-V Instruction Generator
#	Testing your cores, sims and ems made simpler!
#======================================================

# Imports
import os
import click
import sys

# CLI

#!/usr/bin/env python
import argparse
from riscv_instr_gen.utils import RV_instruction_generator

def main():
    parser = argparse.ArgumentParser(description="RISC-V Instruction Generator CLI")
    parser.add_argument("--generate", action="store_true", help="Generate RISC-V instructions")
    parser.add_argument("--isa", help="Specify the ISA format (e.g., RV32I)")
    parser.add_argument("--number", type=int, help="Number of instructions to generate")

    args = parser.parse_args()

    if args.generate:
        if args.isa and args.number is not None:
            isa_format = args.isa
            num_instructions = args.number
            
            instr_generator = RV_instruction_generator(isa_format)
            instr_generator.isa_format_check()

            # Get the list of instruction categories to generate
            instructions_to_generate = instr_generator.get_instructions_to_generate(num_instructions)
            
            for instruction in instructions_to_generate:
                # Print the instruction category and its functions
                category = instruction
                functions = instr_generator.get_functions_by_category(category)
                print(f"Category: {category}\nFunctions: {', '.join(functions)}\n")

if __name__ == "__main__":
    main()
