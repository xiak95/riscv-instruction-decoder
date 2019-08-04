#!/usr/bin/env python3

import argparse
from riscv_opcode import *
from gui import *

parser = argparse.ArgumentParser(prog='riscv-decode.py')
parser.add_argument("-g", "--graphic", help="enable GUI mode", action="store_true")
parser.add_argument("instruction", nargs='?', help="RISC-V Machine level instruction in hex")
#   Parsing arguments
args = parser.parse_args()

if args.graphic:
    # Check for PyGTK support
    try:
        import gi
        gi.require_version('Gtk', '3.0')
        from gi.repository import Gtk

        decoder_main_window = MainWindow()
        if args.instruction is not None:
            decoder_main_window.hex_entry.set_text(args.instruction)

        decoder_main_window.set_icon_from_file("./images/riscv.png")
        decoder_main_window.connect("destroy", Gtk.main_quit)
        decoder_main_window.show_all()
        Gtk.main()
    except ModuleNotFoundError:
        print("Python GTK 3.0 is currently not supported by your system.\nGUI mode disabled.")
        args.graphic = False

else:
    # Check if instruction is in hex
    try:
        instruction = args.instruction
        int(instruction, 16)
    except TypeError:
        parser.print_help()
        exit(0)
    except ValueError:
        exit("Instruction Must be a hex.")
    print("RISC-V 2.2 RV64IMAFD Machine Instruction To Opcode Decoder\n")
    opcode = decode_instruction(instruction)
    if opcode is "ERROR":
        exit("Invalid RV64IMAFD Instruction")
    print("Instruction : 0x", instruction)
    print("Opcode      : ", opcode)
exit(0)




