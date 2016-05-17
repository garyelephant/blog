# Reset specific consumer group of specific topic
# Warn: Please stop consumers before run this script
# pip install kazoo
# https://kazoo.readthedocs.io

import sys
from kazoo.client import KazooClient

if len(sys.argv) not in (3, 4):
    print "usage:"
    print "\t python", sys.argv[0], "zk_connect group [topic]"
    print "\t for example: python", sys.argv[0], "1.2.3.4:2181 mytopic mygroup"
    print "\t Caution: if you do not specify topic name, the whole group will be deleted !"
    sys.exit(1)

zk_connect = sys.argv[1]
group = sys.argv[2]
topic = sys.argv[3] if len(sys.argv) == 4 else None

path = '/consumers/{group}/{type}/{topic}'
top_path = '/consumers/{group}'.format(group=group)

zk = KazooClient(hosts=zk_connect)
zk.start()

if topic is None:
    print "Success: the whole consumer group({group}) is deleted".format(group=group)
    zk.delete(top_path, recursive=True)
    sys.exit(0)

offset_path = path.format(type='offsets', group=group, topic=topic)
if zk.exists(offset_path):
    print offset_path, "exists ! "
    zk.delete(offset_path, recursive=True)

owner_path = path.format(type='owners', group=group, topic=topic)
if zk.exists(owner_path):
    print owner_path, "exists !"
    zk.delete(owner_path, recursive=True)

upper_path = path.format(group=group, type='offsets', topic='')
if zk.exists(upper_path):
    topic_list = zk.get_children(upper_path)
    if len(topic_list) == 0:
        print top_path, "is empty"
        zk.delete(top_path, recursive=True)

zk.stop()

print "Success: consumer group({group}) of topic({topic}) is reset !".format(group=group, topic=topic)

