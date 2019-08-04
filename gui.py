import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from riscv_opcode import *


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="RISC-V Machine Instruction Decoder")
        self.set_border_width(5)
        self.set_default_size(400, 250)

        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.add(main_box)
        main_listbox = Gtk.ListBox()
        main_listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        main_box.pack_start(main_listbox, True, True, 1)

        decoder_label_row = Gtk.ListBoxRow()
        decoder_label_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        decoder_label = Gtk.Label()
        decoder_label.set_markup("<big> <b> RISC-V Machine Instruction Decoder </b></big>")
        decoder_label_box.pack_start(decoder_label, True, True, 10)
        decoder_label_box.set_property("margin-top", 30)
        decoder_label_row.add(decoder_label_box)
        main_listbox.add(decoder_label_row)

        hex_entry_row = Gtk.ListBoxRow()
        hex_entry_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=1)
        hex_entry_label = Gtk.Label("Hex Instruction : ")
        self.hex_entry = Gtk.Entry()
        hex_entry_box.pack_start(hex_entry_label, False, False, 0)
        hex_entry_box.pack_start(self.hex_entry, True, True, 5)
        hex_entry_row.set_property("margin-top", 30)
        hex_entry_row.add(hex_entry_box)
        main_listbox.add(hex_entry_row)

        opcode_entry_row = Gtk.ListBoxRow()
        opcode_entry_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=1)
        opcode_entry_label = Gtk.Label("Opcode : ")
        self.opcode_entry = Gtk.Entry()
        # self.opcode_entry.set_property("text", "NULL")
        self.opcode_entry.set_property("editable", False)
        opcode_entry_box.pack_start(opcode_entry_label, False, False, 0)
        opcode_entry_box.pack_start(self.opcode_entry, True, True, 5)
        opcode_entry_row.set_property("margin-top", 30)
        opcode_entry_row.add(opcode_entry_box)
        main_listbox.add(opcode_entry_row)

        decoder_button_row = Gtk.ListBoxRow()
        decoder_button_box = Gtk.Box()
        decoder_button = Gtk.Button("Decode")
        decoder_button.connect("clicked", self.decode_instruction_gui)
        decoder_button_box.pack_end(decoder_button, False, False, 5)
        decoder_button_box.set_property("margin-top", 30)
        decoder_button_row.add(decoder_button_box)
        main_listbox.add(decoder_button_row)

    def decode_instruction_gui(self, decoder_button):
        instruction = self.hex_entry.get_text()
        # Check if instruction is in hex
        try:
            int(instruction, 16)
        except ValueError:
            self.show_message("Invalid Instruction", "Instruction Must be a hex.")
            return
        opcode = decode_instruction(instruction)
        if opcode is "ERROR":
            self.show_message("Invalid Instruction", "Invalid RV64IMAFD Instruction.")
            self.hex_entry.set_text("")
            return
        self.opcode_entry.set_text(opcode)

    def show_message(self, message, secondary_text):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.OK, message)
        dialog.format_secondary_text(secondary_text)
        dialog.run()
        dialog.destroy()

'''
Reference
----------
 * pack_start(child {Widget}, expand {Bool}, fill{Bool}, padding{int})
 * # To find all properties :-
    for pspec in hex_entry_box.props:
            print(pspec)
 * set_property("propery-name", Value)
 * PyGTK dialog box
    dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.OK,"ERROR")
    dialog.format_secondary_text("Message")
    dialog.run()
    dialog.destroy()

'''