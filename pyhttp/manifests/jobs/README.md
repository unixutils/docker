# Kubernetes Jobs
Jobs are similar to other kubernetes objects such as pods or deployments, but Jobs are run only once. For each job one pod is assigned (unless the pod fails). For instance, if a job spec is created to run 10 jobs, 10 pods are assigned. Once a job is completed, the pods created for the jobs need to be cleaned up manually. 

In this example, we run a cURL request on the already running PyHTP service. We make use of the environmental variables that Kubernetes adds to each pod of the cluster, of all the service names and the ports, to construct the cURL command.

## .spec.completions
Defines how many jobs need to be scheduled. For instance if this value is set to 5, 5 pods are assigned for execution.

## .spec.parallelism
Defines how many jobs are to be run in parallel. For insance if a this is set to 2, 2 pods are spawend simultaneously instead of in a sequence.

## Key points: 
- When *completions* alone is defined, *parallelism* is ignored and pods are created equal to the *completions* number in a sequence. 
- When both *completions* and *parallelism* is specified, pods are created equal to the *completions* number and also in parallel as defined in *parallelism*.
- When *parallelism* alone is defined, this is works as a **work queue**. It is like all pods are trying to achieve the completion of a single task. This means if one of the pods achieve its completion, the other pods need not work futher. In this scenario, even if one pods suceeds, no new pods are assigned. However, the other running pods are not terminated automatically. Its our responsibility to let the pod know that the job is done an it can exit. 
 
Example, lets assume we want to perform a certain task on 30 nodes. We assign a *parallelism* of 5, meaning 5 nodes are spawned and maintained in parallel to perform the task on 30 nodes. If at one point the tasks have been executed on all 30 nodes, the pods should be designed such that it gets notified by an external service that the job is done and that it can exit. On the other hand, Kubernetes will ensure that no new pods are scheduled when one pod suceeds.

[Kubernetes jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/) - Official Documentation


