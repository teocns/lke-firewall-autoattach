A DaemonSet that attaches a Firewall to all Linodes of a Kubernetes cluster and labels the node as schedulable.
Useful to be able to expose services on _NodePort_, such as by attaching a Firewall that allows inbound traffic to ports 30000-32767


####  Docker Hub Image

[teocns/lke-firewall-autoattach](https://hub.docker.com/repository/docker/teocns/lke-firewall-autoattach/general)


####  Usage

The application can be run in a DaemonSet as seen in [this example](https://github.com/teocns/lke-firewall-autoattach/blob/main/examples/daemonset.tf).

###### Environment variables

`LINODE_ACCESS_TOKEN` - Required for performing API calls

`FIREWALL_ID` - The Linode Firewall ID

`POST_OPERATION_NODE_LABELS` - If set, will patch the nodes with the provided key:value label (i.e schedulable:true)

`INSTANCE_LABEL` - Node's label (i.e `lke91873-139045-63e5629d44d5`). Also retrievable by using a `fieldRef` pointing to `spec.nodeName`


.

> A _ConfigMap_ containting kubeconfig must be mounted to `/root/.kube/`.



----

#### Important notes

To ensure reliability of you LKE cluster behind a firewall, ensure that you configure your rules accordingly:


TCP port `10250` inbound from `192.168.128.0/17`, Kubelet health checks

UDP port `51820` inbound from `192.168.128.0/17`, Wireguard tunneling for kubectl proxy

TCP `179` inbound from `192.168.128.0/17`, Calico BGP traffic

TCP/UDP port`30000 - 32767` inbound from `All`, NodePorts for workload Services
