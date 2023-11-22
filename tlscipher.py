#!/usr/local/bin

import requests
from bs4 import BeautifulSoup
import re
import json
import argparse
import os

def get_tls_ciphersuite(tls_version='All', security='secure'):
    try:
        url = f'https://ciphersuite.info/cs/?singlepage=true&security={security}'
        if tls_version not in ['tls10','tls11','tls12','tls13','All']:
            raise ValueError('invalid TLS version. choose from tls10, tls11, tls12, tls13 or All.')

        response = requests.get(url + ('' if tls_version == 'All' else f'&tls={tls_version}'))
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'lxml')
        content = soup.find('div', class_='container').find('div', class_='row flex-row justify-content-center mb-3')
        cipher_list = set(re.split(r'.*(TLS_\w+)', li.text)[1] for li in content.find_all('li'))

        return {tls_version: list(cipher_list)}
    except requests.RequestException as e:
        print(f'error fetching data: {e}')
    except Exception as e:
        print(f'an error occurred: {e}')

def save_to_file(tls_cipher, file_path):
    try:
        with open(file_path, "w") as outfile:
            json.dump(tls_cipher, outfile)
        print(f'file saved to {file_path}')
    except IOError as e:
        print(f'error writing file: {e}')

def main():
    parser = argparse.ArgumentParser(description="fetch and save TLS cipher suites.")
    parser.add_argument('-t', '--tlsversion', dest='tls', default='All', choices=['tls10','tls11','tls12','tls13','All'], help="TLS version")
    parser.add_argument('-s', '--security', dest='sec', default='secure', choices=['secure','recommended','weak','insecure'], help="security level")
    parser.add_argument('-f', '--file', dest='file', help="save to file (provide file path)")
    args = parser.parse_args()

    tls_cipher = get_tls_ciphersuite(args.tls, args.sec)
    if tls_cipher:
        if args.file:
            save_to_file(tls_cipher, args.file)
        else:
            print(tls_cipher)

if __name__ == '__main__':
    main()