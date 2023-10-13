#======================================================
#	RISC-V Instruction Generator
#	Testing your cores, sims and ems made simpler!
#======================================================

# Imports
import os
import click
import sys
# Import the argparse module
import argparse

# ... (rest of your code) ...

# Create a function to generate instructions based on the ISA
def generate_instructions(isa):
    r1 = RV_instruction_generator(isa)
    r1.isa_format_check()
    r1.instr_gen()

# Create the CLI parser
def create_parser():
    parser = argparse.ArgumentParser(description="RISC-V Instruction Generator")
    parser.add_argument(
        "--generate",
        type=str,
        choices=i_list,  # Limit choices to valid instruction types
        help="Specify the instruction type to generate",
    )
    parser.add_argument(
        "--isa",
        type=str,
        required=True,
        help="Specify the RISC-V Instruction Set Architecture (e.g., RV32I, RV64I)",
    )
    return parser

# Main function
def main():
    # Create the CLI parser
    parser = create_parser()

    # Parse command-line arguments
    args = parser.parse_args()

    # If --generate is specified, generate the instructions
    if args.generate:
        print(f"Generating {args.generate} instructions for ISA {args.isa}...")
        generate_instructions(args.isa)
    else:
        print("No instruction type specified. Use --generate to specify an instruction type.")

if __name__ == "__main__":
    main()



# CLI
