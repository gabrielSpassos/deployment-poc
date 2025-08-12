#!/bin/sh

echo "\nStarting infra and services..."

cd infra

rm -rf .terraform .terraform.lock.hcl terraform.*

minikube start --memory=2200 --cpus=4 --driver=docker

minikube update-context

kubectl config use-context minikube

tofu init

tofu apply -auto-approve

cd -

echo ""
echo "\nWaiting for services to be ready..."
sleep 20

mkdir -p logs
nohup kubectl port-forward svc/prometheus-server 30001:80 \
  -n deployment-poc-infra-namespace --address 0.0.0.0 > logs/prometheus.log 2>&1 &

nohup kubectl port-forward svc/grafana 30002:80 \
  -n deployment-poc-infra-namespace --address 0.0.0.0 > logs/grafana.log 2>&1 &

nohup kubectl port-forward svc/jenkins 30003:80 \
  -n deployment-poc-infra-namespace --address 0.0.0.0 > logs/jenkins.log 2>&1 &