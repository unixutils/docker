# Kubernetes Configuration management

Kubernetes provides API objects to attach configurations which can be separately maintained and used with pods/deployments.

## ConfigMaps

ConfigMaps can be used to store key value pairs that does not require any kind of security.

There are four different ways that you can use a ConfigMap to configure a container inside a Pod:

1.  Inside a container command and args
2.  Environment variables for a container
3.  Add a file in read-only volume, for the application to read
4.  Write code to run inside the Pod that uses the Kubernetes API to read a ConfigMap

Check the official Kubernetes Documentation for [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)

Here we have provided with an example ConfigMap config to store key value pairs as Environmental variables and as mounted volumes, in the in PyHTTP deployment.

**Usage :** kubectl apply -f pyhttp-cmap.yml

## Secrets

Secrets are similar to ConfigMaps but instead it is used to sensitve data. Secrets require values to be base64-encoded unless a specific type of secret called StringData secret is used. These base64-encoded strings are decoded automatically in the pod.

Check the official Kubernetes Documentation for [Secrets](https://kubernetes.io/docs/concepts/configuration/Secret/)

Here we have provided with an example Secret to store both encoded and un-encoded strings to be use in the PyHTTP deployment.

**Usage :** kubectl apply -f pyhttp-secret.yml

