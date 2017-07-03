import sys
import argparse
import utils


def main():
    # parse args
    parser = argparse.ArgumentParser(description='Patch given app Info.plist')
    parser.add_argument('path', help='Path to application')
    args = parser.parse_args()

    utils.patch_app(args.path)

if __name__ == "__main__":
   main()
