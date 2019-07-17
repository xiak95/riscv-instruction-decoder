import sys
from riscv_opcode import *

print("RISC-V 2.2 RV64IMAFD Machine Instruction To Opcode Decoder \n")
if len(sys.argv) < 2 :
    exit("Usage python isa.py <Instruction>")
# Check if instruction is in hex form
try:
    int(sys.argv[1],16)
except ValueError:
    exit("Instruction Must be a hex.")

instruction = format(int(sys.argv[1],16),"032b")[::-1] # "032b" is used for 0 padding if hex contains 0's at MSB
opcode = instruction[:7][::-1]  # Reversing the inverted op code .
try:
    opcode = opcodes_dict[opcode]
    function2 = instruction[25:27][::-1]
    function3 = instruction[12:15][::-1]
    function5 = instruction[20:25][::-1]
    function5_amo = instruction[27:][::-1]
    function7 = instruction[25:][::-1]
    function6 = instruction[26:][::-1]
    function12 = instruction[20:][::-1]
except KeyError:
    exit("Inavalid RV64IMAFD Instruction ")

if opcode == "B-type":
    opcode = b_type_function3_dict[function3]
elif opcode == "I-type":
    opcode = i_type_function3_dict[function3]
elif opcode == "I-type-a":
    opcode = i_type_a_function3_dict[function3]
    if opcode == "I-type-a":
        opcode = i_type_a_function6_dict[function6]
elif opcode == "I-type-b":
    opcode = i_type_b_function3_dict[function3]
    if opcode == "I-type-b":
        opcode = i_type_b_function7_dict[function7]
elif opcode == "I-type-f":
    opcode = i_type_f_function3_dict[function3]
elif opcode == "I-type-fen":
    opcode = i_type_fen_function3_dict[function3]
elif opcode == "S-type":
    opcode = s_type_function3_dict[function3]
elif opcode == "S-type-f":
    opcode = s_type_f_function3_dict[function3]
elif opcode == "U-type":
    opcode = u_type_function3_dict[function3]
    if opcode == "U-type":
        opcode = u_type_function12_dict[function12]
elif opcode == "R-type":
    opcode = r_type_function3_dict[function3]
    if opcode == "r_type_0":
        opcode = r_type_0_function7_dict[function7]
    elif opcode == "r_type_1":
        opcode = r_type_1_function7_dict[function7]
    elif opcode == "r_type_2":
        opcode = r_type_2_function7_dict[function7]
    elif opcode == "r_type_3":
        opcode = r_type_3_function7_dict[function7]
    elif opcode == "r_type_4":
        opcode = r_type_4_function7_dict[function7]
    elif opcode == "r_type_5":
        opcode = r_type_5_function7_dict[function7]
    elif opcode == "r_type_6":
        opcode = r_type_6_function7_dict[function7]
    elif opcode == "r_type_7":
        opcode = r_type_7_function7_dict[function7]
elif opcode == "R-type-w":
    opcode = r_type_w_function3_dict[function3]
    if opcode == "r_type_w_0":
        opcode = r_type_w_0_function7_dict[function7]
    elif opcode == "r_type_w_5":
        opcode = r_type_w_5_function7_dict[function7]
elif opcode == "R-type-amo":
    opcode = r_type_amo_function3_dict[function3]
    if opcode == "r_type_amo_2":
        opcode = r_type_amo_2_function5_dict[function5_amo]
    elif opcode == "r_type_amo_3":
        opcode = r_type_amo_3_function5_dict[function5_amo]
elif opcode == "R4-type-fmadd":
    opcode = r4_type_fmadd_function2_dict[function2]
elif opcode == "R4-type-fnmadd":
    opcode = r4_type_fnmadd_function2_dict[function2]
elif opcode == "R4-type-fmsub":
    opcode = r4_type_fmsub_function2_dict[function2]
elif opcode == "R4-type-fnmsub":
    opcode = r4_type_fnmsub_function2_dict[function2]
elif opcode == "R-type-f":
    opcode = r_type_f_function7_dict[function7]
    if opcode == "r_type_f_sgn":
        opcode = r_type_f_sgn_function3_dict[function3]
    elif opcode == "r_type_f_sgnd":
        opcode = r_type_f_sgnd_function3_dict[function3]
    elif opcode == "r_type_f_fl":
        opcode = r_type_f_fl_function3_dict[function3]
    elif opcode == "r_type_f_fld":
        opcode = r_type_f_fld_function3_dict[function3]
    elif opcode == "r_type_f_m":
        opcode = r_type_f_m_function3_dict[function3]
    elif opcode == "r_type_f_md":
        opcode = r_type_f_md_function3_dict[function3]
    elif opcode == "r_type_f_mv":
        opcode = r_type_f_mv_function3_dict[function3]
    elif opcode == "r_type_f_mvd":
        opcode = r_type_f_mvd_function3_dict[function3]
    elif opcode == "r_type_f_0":
        opcode = r_type_f_0_function5_dict[function5]
    elif opcode == "r_type_f_1":
        opcode = r_type_f_1_function5_dict[function5]
    elif opcode == "r_type_f_2":
        opcode = r_type_f_2_function5_dict[function5]
    elif opcode == "r_type_f_3":
        opcode = r_type_f_3_function5_dict[function5]

print("Instruction : 0x",sys.argv[1])
print("Opcode      : ", opcode)
exit(0)
