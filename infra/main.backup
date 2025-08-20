terraform {
  required_providers {
    helm = {
      source  = "hashicorp/helm"
      version = ">= 2.11"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = ">= 2.24"
    }
  }
}

provider "kubernetes" {
  config_path = "~/.kube/config"
}

provider "helm" {
  kubernetes = {
    config_path = "~/.kube/config"
  }
}

resource "kubernetes_namespace" "deployment_poc_application_namespace" {
  metadata {
    name = "deployment-poc-application-namespace"
  }
}

resource "kubernetes_namespace" "deployment_poc_infra_namespace" {
  metadata {
    name = "deployment-poc-infra-namespace"
  }
}

# Grant Jenkins permissions in the deployment-poc-application-namespace namespace
resource "kubernetes_role" "app_admin" {
  metadata {
    name      = "app-admin"
    namespace = kubernetes_namespace.deployment_poc_application_namespace.metadata[0].name
  }

  rule {
    api_groups = ["*"]
    resources  = ["*"]
    verbs      = ["*"]
  }
}

resource "kubernetes_role_binding" "jenkins_app_admin" {
  metadata {
    name      = "jenkins-app-admin"
    namespace = kubernetes_namespace.deployment_poc_application_namespace.metadata[0].name
  }
  role_ref {
    api_group = "rbac.authorization.k8s.io"
    kind      = "Role"
    name      = kubernetes_role.app_admin.metadata[0].name
  }
  subject {
    kind      = "ServiceAccount"
    name      = "default"
    namespace = kubernetes_namespace.deployment_poc_infra_namespace.metadata[0].name
  }
  depends_on = [
    kubernetes_role.app_admin,
    kubernetes_namespace.deployment_poc_application_namespace
  ]
}

# Deploy Prometheus
resource "helm_release" "prometheus" {
  name              = "prometheus"
  chart             = "prometheus"
  repository        = "https://prometheus-community.github.io/helm-charts"
  version           = "27.28.2"
  namespace         = kubernetes_namespace.deployment_poc_infra_namespace.metadata[0].name
  create_namespace  = false
  timeout           = 900 # 15 minutes
  set = [
    {
      name  = "server.service.type"
      value = "NodePort"
    },
    {
      name  = "server.service.nodePort"
      value = "30001"
    }
  ]
}

# Deploy Grafana
resource "helm_release" "grafana" {
  name       = "grafana"
  chart      = "grafana"
  repository = "https://grafana.github.io/helm-charts"
  version    = "9.3.0"
  namespace  = kubernetes_namespace.deployment_poc_infra_namespace.metadata[0].name
  create_namespace  = false
  timeout    = 600 # 10 minutes
  values     = [file("${path.module}/values/grafana.yaml")]
  depends_on = [helm_release.prometheus]
  set        = [
    {
      name  = "service.type"
      value = "NodePort"
    },
    {
      name  = "service.nodePort"
      value = "30002"
    },
    {
      name  = "adminUser"
      value = "admin"
    },
    {
      name  = "adminPassword"
      value = "admin"
    }
  ]
}

# Deploy Docker Registry
resource "helm_release" "docker_registry" {
  name              = "docker-registry"
  chart             = "docker-registry"
  repository        = "https://helm.twun.io"
  namespace         = kubernetes_namespace.deployment_poc_infra_namespace.metadata[0].name
  create_namespace  = false
  timeout           = 600 # 10 minutes
  set = [
    {
      name  = "service.type"
      value = "NodePort"
    },
    {
      name  = "service.nodePort"
      value = "30004"
    },
    {
      name  = "persistence.enabled"
      value = "false"
    }
  ]
}

# Deploy Jenkins
resource "helm_release" "jenkins" {
  name              = "jenkins"
  chart             = "jenkins"
  repository        = "https://charts.jenkins.io"
  namespace         = kubernetes_namespace.deployment_poc_infra_namespace.metadata[0].name
  create_namespace  = false
  version           = "5.8.72"
  timeout           = 900 # 15 minutes
  set        = [
    {
      name  = "controller.serviceType"
      value = "NodePort"
    },
    {
      name  = "controller.servicePort"
      value = "80"
    },
    {
      name  = "controller.nodePort"
      value = "30003"
    },
    {
      name  = "controller.admin.username"
      value = "admin"
    },
    {
      name  = "controller.admin.password"
      value = "admin"
    }
  ]
}
