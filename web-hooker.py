#!/usr/bin/python

import json
import sys
from pygit2 import Repository, Oid, GIT_SORT_TOPOLOGICAL

nil="0000000000000000000000000000000000000000"

payload = dict(zip(('before', 'after', 'ref'), sys.stdin.read().split()))

payload['created'] = True if payload['before'] == nil else False
payload['deleted'] = True if payload['after'] == nil else False

if not payload['created'] and not payload['deleted']:

    repo = Repository('.')

    log = repo.walk(Oid(hex=payload['after']), GIT_SORT_TOPOLOGICAL)
    log.hide(Oid(hex=payload['before']))
    payload['commits'] = []
    for commit in log:
        info = {}
        info['id'] = commit.hex
        info['message'] = commit.message

        author = {}
        author['name'] = commit.author.name
        author['email'] = commit.author.email
        author['timestamp'] = commit.author.time
        info['author'] = author

        committer = {}
        committer['name'] = commit.committer.name
        committer['email'] = commit.committer.email
        committer['timestamp'] = commit.committer.time
        info['committer'] = committer

        payload['commits'].append(info)

print(json.dumps(payload))
