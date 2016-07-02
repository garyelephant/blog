"""
pip install kafka-python
"""

import sys
from kafka import KafkaConsumer, TopicPartition
from kafka.structs import OffsetAndMetadata


if __name__ == '__main__':

    if len(sys.argv) != 4:
        print "usage: python", sys.argv[0], " broker_list topic partition_and_offset"
        # partition_and_offset are partitions you want to set absolute offset, other partitions will not reset offset
        print "\tfor example: python" sys.argv[0], " 10.110.126.190:9092,10.110.126.191:9092 test_topic 1:3684957015,2:3784957015"
        sys.exit(-1)

    broker_list = sys.argv[1].split(',')

    topic_name = sys.argv[2]

    partition_offsets = {}

    for s in sys.argv[3].split(','):

        pid, offset = s.split(':')

        partition_offsets[int(pid)] = long(offset)


    consumer = KafkaConsumer(bootstrap_servers=broker_list)

    # only consume partition 24
    # consumer.assign([TopicPartition(topic_name, 24)])

    offsets = {}
    for pid, offset in partition_offsets:
        offsets[TopicPartition(topic_name, pid)] = OffsetAndMetadata(offset, b'')

    for message in consumer:
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
            message.offset, message.key,
            message.value))
