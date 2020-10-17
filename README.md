# Kubernetes Setup

 * Using AWS EKS 
 * Setup.sh file contain the commands to setup application


## Setup
 * create docker image
 * configure storage class
 * deploy secrets
 * deploy postgresql database
 * deploy goweb application
 * deploy nginx ingress controller
 * deploy alb ingress controller
 * expose nginx ingress


## High Availability

 * replicas are more than one
 * pod anti affinity is setup so that all replicas are spread across nodes
 * tolerations are setup to reduce default eviction time of pods from nodes, incase node goes down
 * deployment strategy is setup as rolling updates and its configured that 2 pods should be available at all times, so the new deployment will happen on pod by pod
 * liveliness and readiness probes are setup, so that if pods are failing no request are sent on it and also previous deployed pods are not terminated until the news ones are healthy
 * We can also configure horizontal pod scaling and cluster autoscaler to increase and decrease the capacity on demand and make it more available
 
## Security
 * Passwords are injected via secrets and these secrets could be managed by a secret controller for eg vault
 * allowPrivilegeEscalation is set as false so container will not be able to elevate its access and privilege
 * Security context is appropriately setup so that container doesnt run as root user user, group and filesystem group is setup for container which has least privilege
 * configuration of container is done in a way that default service account is not attached with pod which has access to talk to kube api server
 * SSL is configured in order to have encrypted communication between client and application
 * We can further use seccomp to filter an elevated system process call
 * We can further use AppArmor to restrict capabilities of individual programs
 
 
 ## Ease of maintainance
 
 * One generic helm chart is created and every a new values.yaml can be given to it in order to deploy and application
 * Flexibility for example, you can enable or disable volumes, volumesMounts, Ingress, PVC as per your choice
 * Normal environment vars as well as sensitive environment vars via secrets can be injected in application 
 
 ## SSL
 * We have nginx ingress controller setup in the cluster that will send request to the appropriate service base on the hostname
 * We have alb ingress controller setup which will create an alb and any request coming onto that will be sent to nginx ingress and eventually to the service
 * nginx ingress is used as a proxy to do host name routing
 * Alb is created and Also an AWS ACM certificate (We can use self signed certificate and offload ssl on ingress level but this is more professional and self signed certificates should be ignored), ssl offloading is done on the alb level providing further security
 * Application is exposed via https
 
 
 ## Update in Dockerfile
 
 * There was no requirement of environment variables as it can directly be injected in Kubernetes manifest that too securely because we are using secrets to inject password
 * We need to download the executable using the curl command 
 * and then using the chmod command so that this executable can be used
 * So CMD and COPY command is als updated check Dockerfile


# Parse JSON
* parse json python script is in hirazon folder
