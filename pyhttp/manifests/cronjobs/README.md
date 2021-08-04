# Kubernetes CronJobs

Kubernetes cronjobs can be compared with crontabs in linux. It does exactly that which a linux cronjob does, but runs out a pod.
Schedules for cronjob takes the same syntax as in a crontab.

In this example, we run a cURL request on the already running PyHTP service. We make use of the environmental variables that Kubernetes adds to each pod of the cluster, of all the service names and the ports, to construct the cURL command. This cURL command is scheduled to run every minute.

## .spec.schedule
Defines the schedule for the job to run.

**Schedule syntax :**


    ┌───────────── minute (0 - 59)
    │ ┌───────────── hour (0 - 23)
    │ │ ┌───────────── day of the month (1 - 31)
    │ │ │ ┌───────────── month (1 - 12)
    │ │ │ │ ┌───────────── day of the week (0 - 6) (Sunday to Saturday;
    │ │ │ │ │                                   7 is also Sunday on some systems)
    │ │ │ │ │
    │ │ │ │ │
    * * * * *
    
    # Example, Run something @ 12:30 on 10th day of all months
    # schedule: "30 12 10 * *" 


## .spec.startingDeadlineSeconds
When a cronjob cannot start as per schedule (for reasons such as, previous job is still running or a downtime) the job will be reattempted continuously until *startingDeadlineSeconds* is reached. If this value is not set, the default behaviour is that if the missed schedules reaches 100, then the reattempts will stop.

## .spec.concurrencyPolicy
Options: "Allow", "Forbid", "Replace", to define weather two schedules can overlap, in case the previous one is still running.

## .spec.successfulJobsHistoryLimit
Defines how many successful jobs to be held back in history. Setting it to 0 cleans up job history soon after the job is completed.

## .spec.failedJobsHistoryLimit
Defines how many failed jobs to be held back in history. Setting it to 0 cleans up job history soon after the job has failed.

## Key points:
- If startingDeadlineSeconds is set to a value less than 10 seconds, the CronJob may not be scheduled. This is because the CronJob controller checks things every 10 seconds.
- Cronjob schedule times are based on the timezone of the kube-controller-manager. Checking clock skew is recommended to avoid failures.
