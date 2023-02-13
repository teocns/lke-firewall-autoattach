import requests

from config import LINODE_ACCESS_TOKEN

import logging

log = logging.getLogger(__name__)

def iter_instances(page=1):
    """
    Iterate over all Linode instances.
    """
    response = requests.get("https://api.linode.com/v4/linode/instances?page=%s" % str(page),headers={
        "Authorization": "Bearer {}".format(LINODE_ACCESS_TOKEN)
    }).json()
    if len(response['data']) == 0:
        return
    yield from response['data']
    yield from iter_instances(page + 1)



def find_instance_id(label):
    """
    Find a Linode instance ID by label.
    """
    for instance in iter_instances():
        if instance['label'] == label:
            return instance['id']
    return None


def attach_firewall(firewall_id, instance_id):
    """
    Attach a firewall to a Linode instance.
    """
    response = requests.post(
        "https://api.linode.com/v4/networking/firewalls/%s/devices" % str(firewall_id),
        headers={
            "Authorization": "Bearer {}".format(LINODE_ACCESS_TOKEN)
        },
        json={
            "type": "linode",
            "id": instance_id
        }
    ).json()
    log.info("Attached firewall %s to instance %s", firewall_id, instance_id)
    assert "entity" in response





    