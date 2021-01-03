#  RISC-V 2.2 Opcode Table
opcodes_dict = {
"0010111" : "AUIPC",
"0110111" : "LUI",
"1100111" : "JALR",
"1101111" : "JAL",
"1100011" : "B-type",
"0000011" : "I-type",
"0100011" : "S-type",
"0100111" : "S-type-f",
"1110011" : "U-type",
"0010011" : "I-type-a",
"0011011" : "I-type-b",
"0000111" : "I-type-f",
"0001111" : "I-type-fen",
"1000011" : "R4-type-fmadd",
"1001111" : "R4-type-fnmadd",
"1000111" : "R4-type-fmsub",
"1001011" : "R4-type-fnmsub",
"0110011" : "R-type",
"1010011" : "R-type-f",
"0111011" : "R-type-w",
"0101111" : "R-type-amo",
}
#   B-type function3 table
b_type_function3_dict = {
"000" : "BEQ",
"001" : "BNE",
"100" : "BLT",
"101" : "BGE",
"110" : "BLTU",
"111" : "BGEU",
}
#   I-type function3 table
i_type_function3_dict = {
"000" : "LB",
"001" : "LH",
"010" : "LW",
"100" : "LBU",
"101" : "LHU",
"110" : "LWU",
"011" : "LD",
}
#   I-type-a function3 table
i_type_a_function3_dict = {
"000" : "ADDI",
"010" : "SLTI",
"011" : "SLTIU",
"100" : "XORI",
"110" : "ORI",
"111" : "ANDI",
"001" : "SLLI",
"101" : "I-type-a",
}
#   I-type-a function6 table
i_type_a_function6_dict = {
"000000" : "SRLI",
"010000" : "SRAI",
}
#   I-type-b function3 table
i_type_b_function3_dict = {
"000" : "ADDIW",
"001" : "SLLIW",
"101" : "I-type-b",
}
#   I-type-b function7 table
i_type_b_function7_dict = {
"0000000" : "SRLIW",
"0100000" : "SRAIW",
}
#   I-type-fen function3 table
i_type_fen_function3_dict = {
"000" : "FENCE",
"001" : "FENCE.I",
}
#   I-type-f function3 table
i_type_f_function3_dict = {
"011" : "FLD",
"010" : "FLW",
}
#   S-type function3 table
s_type_function3_dict = {
"000" : "SB",
"001" : "SH",
"010" : "SW",
"011" : "SD",
}
#   S-type-f function3 table
s_type_f_function3_dict = {
"011" : "FSD",
"010" : "FSW",
}
#   U-type function3 table
u_type_function3_dict = {
"000" : "U-type",
"001" : "CSRRW",
"010" : "CSRRS",
"011" : "CSRRC",
"101" : "CSRRWI",
"110" : "CSRRSI",
"111" : "CSRRCI",
}
#   U-type function12 table
u_type_function12_dict = {
"000000000000" : "ECALL",
"000000000001" : "EBREAK",
}
#   R4-type-fmadd function2 table
r4_type_fmadd_function2_dict = {
"00" : "FMADD.S",
"01" : "FMADD.D",
}
#   R4-type-fnmadd function2 table
r4_type_fnmadd_function2_dict = {
"00" : "FNMADD.S",
"01" : "FNMADD.D",
}
#   R4-type-fmsub function2 table
r4_type_fmsub_function2_dict = {
"00" : "FMSUB.S",
"01" : "FMSUB.D",
}
#   R4-type-fnmsub function2 table
r4_type_fnmsub_function2_dict = {
"00" : "FNMSUB.S",
"01" : "FNMSUB.D",
}
#   R-type function3 table
r_type_function3_dict = {
"000" : "r_type_0",
"001" : "r_type_1",
"010" : "r_type_2",
"011" : "r_type_3",
"100" : "r_type_4",
"101" : "r_type_5",
"110" : "r_type_6",
"111" : "r_type_7",
}
#   R-type-0 function7 table
r_type_0_function7_dict = {
"0000000" : "ADD",
"0100000" : "SUB",
"0000001" : "MUL",
}
#   R-type-1 function7 table
r_type_1_function7_dict = {
"0000000" : "SLL",
"0000001" : "MULH",
}
#   R-type-2 function7 table
r_type_2_function7_dict = {
"0000000" : "SLT",
"0000001" : "MULHSU",
}
#   R-type-3 function7 table
r_type_3_function7_dict = {
"0000000" : "SLTU",
"0000001" : "MULHU",
}
#   R-type-4 function7 table
r_type_4_function7_dict = {
"0000000" : "XOR",
"0000001" : "DIV",
}
#   R-type-5 function7 table
r_type_5_function7_dict = {
"0000000" : "SRL",
"0100000" : "SRA",
"0000001" : "DIVU",
}
#   R-type-6 function7 table
r_type_6_function7_dict = {
"0000000" : "OR",
"0000001" : "REM",
}
#   R-type-7 function7 table
r_type_7_function7_dict = {
"0000000" : "AND",
"0000001" : "REMU",
}
#   R-type-w function3 table
r_type_w_function3_dict = {
"000" : "r_type_w_0",
"001" : "SLLW",
"100" : "DIVW",
"101" : "r_type_w_5",
"110" : "REMW",
"111" : "REMUW",
}
#   R-type-w-0 function7 table
r_type_w_0_function7_dict = {
"0000000" : "ADDW",
"0100000" : "SUBW",
"0000001" : "MULW",
}
#   R-type-w-5 function7 table
r_type_w_5_function7_dict = {
"0000000" : "SRLW",
"0100000" : "SRAW",
"0000001" : "DIVUW",
}
#   R-type-amo function3 table
r_type_amo_function3_dict = {
"010" : "r_type_amo_2",
"011" : "r_type_amo_3",
}
#   R-type-amo-2 function5 table
r_type_amo_2_function5_dict = {
"00010" : "LR.W",
"00011" : "SC.W",
"00001" : "AMOSWAP.W",
"00000" : "AMOADD.W",
"00100" : "AMOXOR.W",
"01100" : "AMOAND.W",
"01000" : "AMOOR.W",
"10000" : "AMOMIN.W",
"10100" : "AMOMAX.W",
"11000" : "AMOMINU.W",
"11100" : "AMOMAXU.W",
}
#   R-type-amo-3 function5 table
r_type_amo_3_function5_dict = {
"00010" : "LR.D",
"00011" : "SC.D",
"00001" : "AMOSWAP.D",
"00000" : "AMOADD.D",
"00100" : "AMOXOR.D",
"01100" : "AMOAND.D",
"01000" : "AMOOR.D",
"10000" : "AMOMIN.D",
"10100" : "AMOMAX.D",
"11000" : "AMOMINU.D",
"11100" : "AMOMAXU.D",
}
#   R-type-f function7 table
r_type_f_function7_dict = {
"0000000" : "FADD.S",
"0000100" : "FSUB.S",
"0001000" : "FMUL.S",
"1111000" : "FMV.W.X",
"0000001" : "FADD.D",
"0000101" : "FSUB.D",
"0001001" : "FMUL.D",
"0100000" : "FCVT.S.D",
"0100001" : "FCVT.D.S",
"1111001" : "FMV.D.X",
"0001100" : "FDIV.S",
"0101100" : "FSQRT.S",
"0001101" : "FDIV.D",
"0101101" : "FSQRT.D",
"0010000" : "r_type_f_sgn",
"1010000" : "r_type_f_fl",
"0010001" : "r_type_f_sgnd",
"1010001" : "r_type_f_fld",
"0010100" : "r_type_f_m",
"0010101" : "r_type_f_md",
"1110000" : "r_type_f_mv",
"1110001" : "r_type_f_mvd",
"1100000" : "r_type_f_0",
"1100001" : "r_type_f_1",
"1101000" : "r_type_f_2",
"1101001" : "r_type_f_3",
}
#   R-type-f-sgn function3 table
r_type_f_sgn_function3_dict = {
"000" : "FSGNJ.S",
"001" : "FSGNJN.S",
"010" : "FSGNJX.S",
}
#   R-type-f-sgnd function3 table
r_type_f_sgnd_function3_dict = {
"000" : "FSGNJ.D",
"001" : "FSGNJN.D",
"010" : "FSGNJX.D",
}
#   R-type-f-fl function3 table
r_type_f_fl_function3_dict = {
"010" : "FEQ.S",
"001" : "FLT.S",
"000" : "FLE.S",
}
#   R-type-f-fld function3 table
r_type_f_fld_function3_dict = {
"010" : "FEQ.D",
"001" : "FLT.D",
"000" : "FLE.D",
}
#   R-type-f-m function3 table
r_type_f_m_function3_dict = {
"001" : "FMAX.S",
"000" : "FMIN.S",
}
#   R-type-f-md function3 table
r_type_f_md_function3_dict = {
"001" : "FMAX.D",
"000" : "FMIN.D",
}
#   R-type-f-mv function3 table
r_type_f_mv_function3_dict = {
"001" : "FMV.X.W ",
"000" : "FCLASS.S",
}
#   R-type-f-mvd function3 table
r_type_f_mvd_function3_dict = {
"001" : "FCLASS.D",
"000" : "FMV.D.X",
}
#   R-type-f-0 function5 table
r_type_f_0_function5_dict = {
"00010" : "FCVT.L.S",
"00011" : "FCVT.LU.S",
"00000" : "FCVT.W.S",
"00001" : "FCVT.WU.S",
}
#   R-type-f-1 function5 table
r_type_f_1_function5_dict = {
"00010" : "FCVT.L.D",
"00011" : "FCVT.LU.D",
"00000" : "FCVT.W.D",
"00001" : "FCVT.WU.D",
}
#   R-type-f-2 function5 table
r_type_f_2_function5_dict = {
"00010" : "FCVT.S.L",
"00011" : "FCVT.S.LU",
"00000" : "FCVT.S.W",
"00001" : "FCVT.S.WU",
}
#   R-type-f-3 function5 table
r_type_f_3_function5_dict = {
"00010" : "FCVT.D.L",
"00011" : "FCVT.D.LU",
"00000" : "FCVT.D.W",
"00001" : "FCVT.D.WU",
}


def decode_instruction(instruction):
    instruction = format(int(instruction, 16), "032b")[::-1]  # "032b" is used for 0 padding if hex contains 0's at MSB
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

        print("opcode is " +opcode )
        print("function2 is " +function2 )
        print("function3 is " +function3 )
        print("function5 is " +function5 )
        print("function5_amo is " +function5_amo )
        print("function7 is " +function7 )
        print("function6 is " +function6 )
        print("function12 is " +function12 )
    except KeyError:
        return "ERROR"

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
    return opcode