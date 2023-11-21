import argparse
from pathlib import Path

from GcodeParser.gparser.gparser import GcodeParser
from match_gcode import header_gparser, footer_gparser, replacing_header_gparser


def replaceing_initial_gcode(
        gparser: GcodeParser,
        init_gparser: GcodeParser,
        replacing_gparser: GcodeParser,
        del_lines_n: int
):
    # search delete gcode
    offsets_i = gparser.match_lines(init_gparser, first_only=True)

    assert offsets_i, f'not matching\n{init_gparser}'
    offset_i = offsets_i[0]

    # delete gcode
    del gparser.glines[offset_i:offset_i + del_lines_n]

    # add initial gcode
    for i, gline in enumerate(replacing_gparser.glines):
        gparser.glines.insert(i + offset_i, gline)


def delete_gcode(
        gparser: GcodeParser,
        del_gparser: GcodeParser,
        del_lines_n: int
):
    # search delete gcode
    offsets_i = gparser.match_lines(del_gparser, first_only=True)

    assert offsets_i, f'not matching\n{del_gparser}'
    offset_i = offsets_i[0]

    # delete gcode
    del gparser.glines[offset_i:offset_i + del_lines_n]


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--dir", type=Path, help="directry containing nc(gcode) file")
    parser.add_argument("-f", "--file", type=Path, nargs='+',
                        help="nc(gcode) file. If multiple items are specified, separate them with a ','(comma)")

    return parser.parse_args()


def main():
    args = parse_args()
    assert not ((args.dir is None) and (args.file is None)), "require -d or  w-f option"

    files_path = args.file
    if files_path is None:
        files_path = list(args.dir.glob('*.nc'))

    assert files_path, "not found nc file"

    print(f'\nfile: {files_path}\n')
    gparsers = [GcodeParser.from_flatcam(path) for path in files_path]

    if len(gparsers) == 1:
        replaceing_initial_gcode(gparsers[0], header_gparser, replacing_header_gparser, 16)
        gparsers[0].save(Path('test.nc'))

    else:
        replaceing_initial_gcode(gparsers[0], header_gparser, replacing_header_gparser, 16)
        delete_gcode(gparsers[0], footer_gparser, len(footer_gparser))

        for gparser in gparsers[1:-1]:
            delete_gcode(gparser, header_gparser, 16)
            delete_gcode(gparser, footer_gparser, len(footer_gparser))

        delete_gcode(gparsers[-1], header_gparser, 16)

        out_gparser = GcodeParser([])
        for gparser in gparsers:
            out_gparser.glines.extend(gparser.glines)

        out_gparser.save(Path('test.nc'))


if __name__ == "__main__":
    main()
