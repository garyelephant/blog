"""
requirements:

pip install kafka-python
"""

from kafka import KafkaConsumer


if __name__ == '__main__':
    import sys
    topic, consumer_group, bootstrap_servers = sys.argv[1:]

    # To consume latest messages and auto-commit offsets
    consumer = KafkaConsumer(topic,
        group_id=consumer_group,
        bootstrap_servers=bootstrap_servers.split(","))

    for message in consumer:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        print ("partition=%d offset=%d key=%s value=%s" % (
            message.partition,
            message.offset,
            message.key,
            message.value
        ))
