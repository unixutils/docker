# Important elements in a service manifest
- *`apiVersion`* (v1)
- *`kind`* (Service)
- *`metadata.name`* (name of the service object)
- *`metadata.labels`* (key value pairs as labels for the service object)
- *`spec.type`* (type of service such as LoadBalancer, NodePort etc)
- *`spec.selector`* (key value pairs to look for in the deployment that the service will expose)
- *`spec.ports.port`* (port listened by pod. Pod redirects traffic received on port to targetPort)
- *`spec.ports.targetPort`* (port listened by container in a pod)
>NOTE: By default and for convenience, the `.targetPort` is set to the same value as the `.port` field.
