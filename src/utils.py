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


class RV_instruction_generator:
    def __init__(self, isa):
        self.isa = isa
        self.isa_format_check()  # Check the format when the object is created

    def isa_format_check(self):
        # Check if the ISA format is valid
        error_flag = True
        for bw in list_bit_width:
            match = re.search(f"RV{bw}[IA]", self.isa)
            if match:
                error_flag = False  # Valid format found
                break
        if error_flag:
            print("Enter a valid ISA Extension!")
            sys.exit(1)

    def instr_gen(self):
        ext = list(self.isa)[2:]
        ext_list = list(ext)  # List of extensions

        with open("assemblyfile.s", "w") as file:
            for ext_i in i_list:
                if ext_i in i_ext_list:
                    if isinstance(i_ext_list[ext_i], list):
                        for instr in i_ext_list[ext_i]:
                            file.write(instr + "\n")
                    else:
                        file.write(i_ext_list[ext_i] + "\n")

# Example usage
isa_test = "RV32I"
r1 = RV_instruction_generator(isa_test)
r1.instr_gen()
