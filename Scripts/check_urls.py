#!/usr/bin/env python3
import requests
from glob import glob
from urllib.request import urlopen
from urllib.error import URLError
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

log_file = f"check-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"
log = open(log_file, 'w')
log_lock = Lock()

def check_url(url):
    try:
        if url.startswith('ftp://'):
            urlopen(url, timeout=10)
            print(f"✓ FTP {url}")
        else:
            r = requests.head(url, timeout=10)
            if r.ok:
                print(f"✓ {r.status_code} {url}")
            else:
                with log_lock:
                    log.write(f"✗ {r.status_code} {url}\n")
    except (URLError, Exception) as e:
        with log_lock:
            log.write(f"✗ ERROR {url}: {e}\n")

# Collect all URLs
urls = []

with open('BioTuring/benchmark.txt') as f:
    for line in f:
        if line.strip() and not line.startswith('#'):
            urls.append(line.strip().split('\t')[2])

for file in glob('BioTuring/sequence.index*'):
    with open(file) as f:
        for i, line in enumerate(f):
            if i == 0 or not line.strip():
                continue
            parts = line.strip().split('\t')
            for part in parts:
                if part.startswith(('ftp://', 'http://', 'https://')):
                    urls.append(part)

# Check URLs in parallel
with ThreadPoolExecutor(max_workers=40) as executor:
    futures = [executor.submit(check_url, url) for url in urls]
    for future in as_completed(futures):
        future.result()

log.close()
print(f"\nChecked {len(urls)} URLs. Errors logged to: {log_file}")
