
Docker Hub Image

[teocns/lke-firewall-autoattach](https://hub.docker.com/repository/docker/teocns/lke-firewall-autoattach/general)

___

Auto-attach a Linode Firewall to all Linodes of a Kubernetes cluster

Useful to be able to expose services on _NodePort_



---

The application can be run in a DaemonSet as seen is this example by providing the following environment variables:

`LINODE_ACCESS_TOKEN` - Required for performing API calls

`FIREWALL_ID` - The Linode Firewall ID

`POST_OPERATION_NODE_LABELS` - If set, will patch the nodes with the provided key:value label (i.e schedulable:true)

`INSTANCE_LABEL` - Node's label (i.e `lke91873-139045-63e5629d44d5`). Also retrievable by using a `fieldRef` pointing to `spec.nodeName`

---


Lastly, a _ConfigMap_ containting kubeconfig must be mounted to `/root/.kube/`.



`


`

