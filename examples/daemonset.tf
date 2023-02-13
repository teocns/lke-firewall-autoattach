# Ensure that all nodes run a copy of the firewall

resource "kubernetes_daemonset" "lke_firewall_autoattach" {
  metadata {
    name      = "lke-firewall-autoattach"
    namespace = "kube-system"
  }

  spec {
    selector {
      match_labels = {
        name = "lke-firewall-autoattach"
      }
    }

    template {
      metadata {
        labels = {
          name = "lke-firewall-autoattach"
        }
      }
      spec {
        host_pid     = true
        host_ipc     = true
        host_network = true
        
        container {
          name  = "lke-firewall-autoattach"
          image = "teocns/lke-firewall-autoattach:latest"

          
          env {
            name = "INSTANCE_LABEL"
            value_from {
              field_ref {
                field_path = "spec.nodeName"
              }
            }
          }

          env {
            name = "FIREWALL_ID"
            value = var.FIREWALL_ID
          }

          env {
            name = "LINODE_ACCESS_TOKEN"
            value = var.LINODE_TOKEN
          }

          env {
            name = "POST_OPERATION_NODE_LABELS"
            value = "schedulable:true"
          }
          volume_mount {
            name       = "kubeconfig"
            mount_path = "/root/.kube"
          }
        }

        volume {
          name = "kubeconfig"
          config_map {
            name = kubernetes_config_map.kubeletconfig.metadata.0.name
          }
        }
      }
    }
  }
}


