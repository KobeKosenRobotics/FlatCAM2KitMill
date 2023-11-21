from GcodeParser.gparser.gparser import GcodeParser


init_binary = """G21
G90
G94

G01 F100.00

M5
G00 Z15.0000
G00 X0.0000 Y0.0000"""

end_binary = """M05
G00 Z3.0000
G00 Z5.00


M30"""

replacing_init_binary = """G21
G61
G90
G94

G00 Z15.0000
G00 X0.0000 Y0.0000

M03"""

header_gparser = GcodeParser.from_flatcam_bynary(init_binary)
footer_gparser = GcodeParser.from_flatcam_bynary(end_binary)

replacing_header_gparser = GcodeParser.from_flatcam_bynary(replacing_init_binary)
