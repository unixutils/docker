# Elements in a deployment manifest
- *apiVersion* (apps/v1)
- *kind* (deployment)
- *metadata.name* (name of the deployment object)
- *metadata.labels* (key value pairs as labels for the deployment object)
- *spec.replicas* (replca count of pods)
- *spec.selector.matchLabels* (key value pairs to look for in the pod that the deployment will control)  

>NOTE: removing/modifying the matched label on a pod after its deployment controller has brought it up, would orphen the pod.
- *template.metadata.labels* (key value pairs to put on the pod when its brought up by the deployment)
- *template.spec.containers* (container spec such as name, image, ports etc)
