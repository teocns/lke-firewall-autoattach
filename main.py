
from config import FIREWALL_ID, INSTANCE_LABEL, POST_OPERATION_NODE_LABELS
import signal

from linode import find_instance_id, attach_firewall
from k8s import set_node_label
import logging

log = logging.getLogger(__name__)

def main():

    assert FIREWALL_ID is not None and INSTANCE_LABEL is not None, "FIREWALL_ID and INSTANCE_LABEL must be set as environment variables"

    # Find the Linode ID by the Node label
    instance_id = find_instance_id(INSTANCE_LABEL)

    # Attach the firewall to the Linode instance
    attach_firewall(FIREWALL_ID, instance_id)

    # Set the Node label to indicate that the firewall has been attached, if set

    if POST_OPERATION_NODE_LABELS is not None:
        # Format is key:value
        key, value = POST_OPERATION_NODE_LABELS.split(":")
        set_node_label(INSTANCE_LABEL, key, value)

    # Sleep forever
    signal.pause()


if __name__ == "__main__":
    main()


