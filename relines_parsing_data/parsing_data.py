import argparse
import requests
from bs4 import BeautifulSoup


def parse_cmd_args():
    """Adding input arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, type=str)
    parser.add_argument("--width", default=70, type=int)
    parser.add_argument("--link", default="True", type=str, choices=["True", "False"])
    parser.add_argument("--result", default="True", type=str, choices=["True", "False"])
    args = parser.parse_args()
    return args

def parsing_site(parsed_args):
    """Getting data from url"""
    url = parsed_args.url
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        return response, soup
    except:
        print("Error: 404 Not Found")
        exit()

if __name__ == "__main__":
    parsed_args = parse_cmd_args()
    response, soup = parsing_site(parsed_args)
