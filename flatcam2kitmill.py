import argparse
from pathlib import Path


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
    breakpoint()
    if files_path is None:
        files_path = list(args.dir.glob('*.nc'))

    assert files_path, "not found nc file"

    print(files_path)


if __name__ == "__main__":
    main()
