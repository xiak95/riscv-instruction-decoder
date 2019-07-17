# RISC-V Instruction Decoder
Very simple RISC-V machine instruction decoder , written in python .Mainly aiming to understand how to decode RISC-V ISA . Currently only supports RV64IMAFD instructions only.

### Features
 - Supports RISC-V RV64IMAFD instructions.
 - Uses spec 2.2 .

## Usage
```sh
$ python3 riscv-decode.py < Machine Instruction >
```
## Example
```sh
$  python3 riscv-decode.py 81818513
RISC-V 2.2 RV64IMAFD Machine Instruction To Opcode Decoder 

Instruction : 0x 81818513
Opcode      :  ADDI
```

