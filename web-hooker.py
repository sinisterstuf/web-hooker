#!/usr/bin/python

import json
import sys

payload = dict(zip(('before', 'after', 'ref'), sys.stdin.read().split()))

print(json.dumps(payload))
