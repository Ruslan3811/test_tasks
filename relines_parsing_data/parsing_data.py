import argparse


def parse_cmd_args():
    """Adding input arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, type=str)
    parser.add_argument("--width", default=70, type=int)
    parser.add_argument("--link", default="True", type=str, choices=["True", "False"])
    parser.add_argument("--result", default="True", type=str, choices=["True", "False"])
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    parsed_args = parse_cmd_args()
