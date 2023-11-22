# tls cipher grabber

this little script is like a treasure map for tls cipher suites. it dives into the vast ocean of ciphersuite.info and brings back pearls of info about tls cipher suites, sorting them into neat piles of 'secure', 'weak', and 'not-so-great'.

## what's this all about?

- **grabbing tls ciphers**: you can pick a tls version (like tls1.2 or tls1.3) and a security level ('secure', 'weak', etc) and this script fetches those ciphers for you.
- **saving the results**: if you wanna keep a record of these ciphers, the script can save them in a json file.
- **easy!**: it's all CLI, straightforward, great for quick lookups or slotting into bigger projects.

## how to run

1. **clone this repo**: snag the code onto your local machine.
2. **fire up the script**: something like `python3 tls_cipher_fetcher.py -t tls12 -s secure` gets you all the secure tls1.2 ciphers.
3. **save your finds**: throw in `-f yourfilename.json` to save the output in a json file.

## stuff you need

- python3
- requests
- beautifulsoup4
- lxml
- argparse

don't worry, there's a requirements file in here. just run `pip install -r requirements.txt` and you're good.

## examples
```bash
python3 tls_cipher_fetcher.py -t tls12 -s secure
```
```css
secure: {'tls12': ['TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384', 'TLS_DHE_RSA_WITH_AES_256_GCM_SHA384', ... ]}
```

```bash
python3 tls_cipher_fetcher.py -t tls13 -s weak
```
```css
weak: {'tls13': ['TLS_AES_128_GCM_SHA256', 'TLS_CHACHA20_POLY1305_SHA256', ... ]}
```

```bash
python3 tls_cipher_fetcher.py -t tls12 -s secure -f secure_tls12.json
```
```css
File saved to secure_tls12.json
```