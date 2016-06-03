# pip install requests

import sys
import time
import requests

if len(sys.argv) != 3:
    print "usage: python", sys.argv[0], "es_host check_interval_in_seconds"
    print "\t for example: python", sys.argv[0], "10.148.18.110:9200 5"
    sys.exit(1)

es_host = sys.argv[1]
check_interval = float(sys.argv[2])


last_rejected = {}
while True:
    resp = requests.get('http://{es_host}/_nodes/stats/thread_pool'.format(es_host=es_host))
    stats = resp.json()
    for nodeid, nodeinfo in stats['nodes'].items():
        name = nodeinfo['name']
        rejected = nodeinfo['thread_pool']['bulk']['rejected']
        if name not in last_rejected:
            last_rejected[name] = rejected

        print name, ":", rejected - last_rejected[name]

        last_rejected[name] = rejected

    print "--------\n"
    time.sleep(check_interval)
