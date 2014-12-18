#!/usr/bin/python

import json
import sys

nil="0000000000000000000000000000000000000000"

payload = dict(zip(('before', 'after', 'ref'), sys.stdin.read().split()))

payload['created'] = True if payload['before'] == nil else False
payload['deleted'] = True if payload['after'] == nil else False

print(json.dumps(payload))
