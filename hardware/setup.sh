#!/usr/bin/env bash
# oc login

kubectl apply -f ti-0-exporter.yaml
kubectl get -n jumpstarter-qemu-exporter secrets ti-0-exporter -o 'jsonpath={.data.token}' | base64 -d
