# Deployment POC

Build a deployment system with:
- Jenkins
- Helm
- OpenTofu
- Minikub or other kubernetes cluster manager
- Prometheus
- Grafana 

You need to be able to deploy an application with all this tools and you need 2 clusters (or2 namespaces) one for the infra and other for the apps that will be deployed.

The pipelines in Jenkins need to run tests and fail if tests fail. 

OpenTofu need to have automated tests as well, all apps deployed need to be integrated with Grafana and Prometheus by default.

* Get minikube status and start
```bash
minikube status
minikube start --driver=docker
```

* Get nodes
```bash
kubectl get nodes -A
```

* Get pods
```bash
kubectl get pods -A
```

* Get deployments
```bash
kubectl get deployments -A
```

* Get services
```bash
kubectl get services -A
```

* Get details on services
```bash
kubectl describe service grafana -n deployment-poc-infra-namespace
kubectl describe service prometheus-server -n deployment-poc-infra-namespace
```

* Get statefulset
```bash
kubectl get statefulsets -A
```

* Get daemonset
```bash
kubectl get daemonset -A
```