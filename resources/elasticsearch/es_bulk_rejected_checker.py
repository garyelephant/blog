# pip install requests

import requests
import time

last_rejected = {}
while True:
    resp = requests.get('http://10.148.18.110:9200/_nodes/stats/thread_pool')
    stats = resp.json()
    for nodeid, nodeinfo in stats['nodes'].items():
        name = nodeinfo['name']
        rejected = nodeinfo['thread_pool']['bulk']['rejected']
        if name not in last_rejected:
            last_rejected[name] = rejected

        print name, ":", rejected - last_rejected[name]

        last_rejected[name] = rejected

    print "--------\n"
    time.sleep(5)
