#
#  Utils for RIG
#

# ------- Imports -------
import os
import sys
import re

# ------- Allowed lists -------
list_bit_width = [32, 64]         # List of allowed bit widths
list_extension = ["I", "A"]       # List of allowed extensions

# ------- Register file -------
reg_file = []
for reg in range(0,32):
    reg_file.append("x"+str(reg)) # x0 - x31 (32 registers)


# ------- Instructions dict -------
i_ext_list = {
               "lui" : "lui",
               "auipc" : "auipc",
               "jal" : "jal",
               "jalr" : "jalr",
               "branch" : ["beq", "bne", "blt", "bge", "bltu", "bgeu"],
               "load_32" : ["lb", "lh", "lw", "lbu", "lhu"],
               "store_32" : ["sb", "sh", "sw"],
               "imm_32" : ["addi", "slti", "sltiu", "xori", "ori", "andi"],
               "shift_imm_32" : ["slli", "srli", "srai"],
               "al_op_32" : ["add", "sub", "sll", "slt", "sltu", "xor", "srl", "sra", "or", "and"],
               "load_64" : ["lwu", "ld"],
               "store_64" : "sd",
               "shift_imm_64" : ["slli", "srli", "srai", "slliw", "srliw", "sraiw"],
               "imm_64" : "addiw",
               "al_op_64" :["addw", "subw", "sllw", "srlw", "sraw"]
             }

i_list = ["lui", "auipc", "jal", "jalr", "branch", "load_32", "store_32", "imm_32",
          "shift_imm_32", "al_op_32", "load_64", "store_64", "shift_imm_64", "imm_64", "al_op_64"]
#i_list_32 = i_list_64[:10]

# ------- Classes -------
class RV_instruction_generator:
    # init func
    def __init__(self, isa):
        self.isa = isa

    # ISA match
    def isa_format_check(self):
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
            sys.exit(0)

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
            sys.exit(0)

    # Instruction generator function
    def instr_gen(self):
       ext = list(self.isa)[4:]
       ext_list = list(ext)       # List of extensions

       xlen = self.isa[2:4]       # XLEN -> 32, 64

       if len(ext_list) > 1:
           for exten in ext_list:
               pass
       else:
           for ext_i in i_list:
               print(ext_i)

    def get_instructions_to_generate(self, num_instructions):
        # Return a list of instruction categories to generate
            if num_instructions <= len(i_list):
                return i_list[:num_instructions]
            else:
                print(f"Warning: Only {len(i_list)} instructions available. Generating all instructions.")
                return i_list

    def get_functions_by_category(self, category):
        # Return a list of functions in the specified category
        if category in i_ext_list:
            functions = i_ext_list[category]
            if isinstance(functions, list):
                return functions
            else:
                return [functions]
        else:
            return []
       
       
# isa_test = "RV32I"
# r1 = RV_instruction_generator(isa_test)
# r1.isa_format_check()
# r1.instr_gen()
