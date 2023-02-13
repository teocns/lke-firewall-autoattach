from kubernetes import client, config


config.load_kube_config()

v1_core = client.CoreV1Api()


def set_node_label(node, key, value):
    """
    Sets a label on a Node
    """
    v1_core.patch_node(node, {"metadata": {"labels": {key: value}}})
