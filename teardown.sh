#!/bin/bash
kubectl delete svc $(kubectl get svc | grep takehomeapi | awk {'print $1'})
kubectl delete deployment takehomeapi
