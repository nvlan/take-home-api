#!/bin/bash

#set -x
function check_kubectl_is_installed {
  command -v kubectl >/dev/null 2>&1 || { error >&2 "I require kubectl but it's not installed. Aborting."; exit 1; }
}

function check_minikube_is_installed {
  command -v minikube >/dev/null 2>&1 || { error >&2 "I require minikube but it's not installed. Aborting."; exit 1; }
}

function check_docker_compose_is_installed {
  command -v docker-compose >/dev/null 2>&1 || { error >&2 "I require docker-compose but it's not installed. Aborting."; exit 1; }
}

function check_minikube_is_running {
  status=$(minikube status | grep host | awk -F ": " {'print $2'})
  if [ $status != "Running" ]; then
    error "Minikube is not running, please start it and try again"
    exit 1
  fi
}

# FUNCION PARA IMPRIMIR MENSAJES DE USER-INPUT
function input {
  RED='\033[0;36m'
  NC='\033[0m' # No Color
  echo "${RED}[ USER ]${NC} - $1"
}

# FUNCION PARA IMPRIMIR MENSAJES DE ERROR
function error {
  RED='\033[0;31m'
  NC='\033[0m' # No Color
  echo "${RED}[ ERROR ]${NC} - $1"
}

# FUNCION PARA IMPRIMIR MENSAJES DE INFO
function info {
  GREEN='\033[0;32m'
  NC='\033[0m' # No Color
  echo "${GREEN}[ INFO ]${NC} - $1"
}

#MAIN
info "Starting pre-deploy checks..."
check_kubectl_is_installed
check_minikube_is_installed
check_docker_compose_is_installed
check_minikube_is_running

info "All checks have passed!"
input "Please, tell me the IP address of this host: "
read -p "- " ip
info "Starting build and push..."
eval $(minikube -p minikube docker-env)
docker build . -t takehomeapi

OS=$(uname -s)
if [ $OS == "Darwin" ]; then
  sed -i '' "s/ip: $PARTITION_COLUMN.*/ip: \"$ip\"/g" deployment.yml
else
  sed -i "s/ip: $PARTITION_COLUMN.*/ip: \"$ip\"/g" deployment.yml
fi

info "Starting deploy to minikube..."
kubectl apply -f deployment.yml
rs=$(kubectl get rs | grep takehomeapi | awk {'print $1'})
kubectl expose rs ${rs} --type=NodePort
url=$(minikube service ${rs} --url)
info "Done! connect using ${url}"
