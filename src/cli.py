import argparse
import random
from utils import RV_instruction_generator  # Import the RV_instruction_generator from your utils.py

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

            # Get a list of categories to generate
            categories_to_generate = instr_generator.get_instructions_to_generate(num_instructions)

            for category in categories_to_generate:
                # Get a random function from the category
                functions = instr_generator.get_functions_by_category(category)
                if functions:
                    random_function = random.choice(functions)
                    print(f"{random_function}\n ")

if __name__ == "__main__":
    main()