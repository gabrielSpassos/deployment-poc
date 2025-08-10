#!/bin/sh

echo "\nStarting infra and services..."

minikube start --driver=docker

kubectl config use-context minikube

tofu init

tofu apply -auto-approve

echo "\nWaiting for services to be ready..."
sleep 20
