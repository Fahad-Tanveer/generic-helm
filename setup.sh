#!/usr/bin/env bash


#creating docker image
curl -L https://github.com/s-marchenko/postgresql-go/releases/download/v1.0.0/website_linux_amd64 --output postgresql
chmod 775 postgresql
docker build -t goweb:1.0 .

#configure storage class for dynamic volume provisioning
kubectl apply -f resources/storageclass.yaml

#configuring secrets
kubectl apply -f resources/secret.yaml

#configuring postgresql database
helm install --name postgresql generic-helm -f postgresql/values.yaml

#configuring go web application
helm install --name postgresql generic-helm -f goweb/values.yaml

#configuring nginx ingress
helm install stable/nginx-ingress --name nginx-ingress --namespace kube-system

#configuing alb ingress controller
kubectl apply -f resources/alb-ingress-controller.yaml


#configuring ingress for alb
kubectl apply -f resources/alb+ingress.yaml
