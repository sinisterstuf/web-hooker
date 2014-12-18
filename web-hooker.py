#!/usr/bin/python

import json
import sys

payload = dict(zip(('old', 'new', 'ref'), sys.stdin.read().split()))

print(json.dumps(payload))
