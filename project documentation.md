Deploy Dockerized Application to Kubernetes

Ticket-1: Configure a Local Docker Registry on Kubernetes Task: Set up a local Docker registry hosted on a Kubernetes cluster.

Created an eks cluster called ope-cluster on aws

![alt text](<0.2a create an eks cluster on aws.png>)

Updated the kubeconfig file on the eks cluster on aws to point towards the cluster created.

![alt text](<0.4a update the kubeconfig file on aws eks cluster.png>)

Created a secret within the kubernetes cluster called docker-registry-secret to login into the docker registry 

![alt text](<0.5a create a secret for the docker registry.png>)

Created a deployment and secret manifest file called docker-registry. Ensure the deployment manifest file has imagePullSecrets included in the deployment manifest file. Run the kubectl commands to confirm the secret, run the deployment and serivce manifest files and confirm the pods and services are running succesfully.

![alt text](<0.6a create a deployment and service manifest files.png>)

![alt text](<0.7a deployment and service manifest file command.png>)

Ensured access into the docker registry from my local machine and within the Kubernetes cluster.

![alt text](<0.9a Ensure you can access the registry from your local machine and within the Kubernetes cluster..png.png>)


Ticket-2: Deploy a Python Web Application to Kubernetes. Accessing the root URL of the application should display a "Hello Kube" message.

Wrote a simple python app whiich displays the  mesage "hello kube"

![alt text](<0.10 write a simple python app whiich displays the  mesage "hello kube"-1.png>)


Dockerise the python application within the same directory as the python app

![alt text](<0.11 dockerise the python application within the same directory as the pthon app.png>)


Build the dockerised python application and push to the docker registry.

![alt text](<0.12 build the dockerise web application and push to the docker registry.png>)


Confirmed the image within the docker registry, ran kubectl get svc, and  used the external IP and port 5000 on the url to confirm the web page is running. Verified access to the application on my local machine's browser.

![alt text](<0.13a confirm the image within the  docker registry.png>)

![alt text](<0.13b Run kubectl get svc, and  use the externalip and port 5000 on the url external IP and the port to confirm the web page is running.png>)

[text](<../../../Pictures/Screenshots/adds_on_prj1/0.13c Verified  access to the application on my local machine's browser>)


Ticket-3: Create a Helm Chart for the Web Application. Develop a Helm chart that can be used to deploy the web application to Kubernetes.

Created an helm chart called 1 by running the command 'helm create 1'

![alt text](<0.14a create an helm chart called 1.png>)

Created an helm template for deployment, service and values manifest files.

![alt text](<0.14b created an helm template for deployment file.png>)

![alt text](<0.15 helm template for service manifest file.png>)

![alt text](<0.16a values file within helm chart.png>)

Validated the yaml files produced for the helm chart by running the command 'helm template -f <path of the values.yaml file> <path of the Chart.yaml file>

![alt text](<0.17a validate the yaml files produced for the helm chart.png>)

![alt text](<0.17b validate the yaml files produced for the helm chart.png>)

Run helm install and confirm it is working  run helm ls and kubectl get pods to confirm the pods are running

![alt text](<0.20a Run helm install and confirm it is working  run helm ls and kubectl get pods to confirm the pods are running.png>)


 Ticket-4: Automate Deployment with Ansible. Use Ansible to automate the deployment of the web application.

Modified the application to display "Hello {{ENV}} Kube," where {{ENV}} depends on the environment (dev, uat, prod).


![alt text](<0.21  modified the application to display "Hello {{ENV}} Kube," where {{ENV}} depends on the environment (dev, uat, prod)..png>)

Rebuilt the modified appplication and pushed to the docker registry, reinstalled the helm chart for the modified application

Modified the deployment manifest file to include env variabe for dev, uat, and prod

![alt text](<0.24a modify the deployment manifest file to include env parameter for dev, uat and prod.png>)

Updated the helm template for deployment to include env for dev, uat, prod. 

![alt text](<0.25a update the helm template for deployment to include env  for dev, uat, prod, .png>)

26a Wrote an ansible playbook to Setup Kubernetes Namespaces and Secrets for Web Deployment,  created Docker registry secret for dev, uat and prod  namespaces and  deployment of helm chart for dev, uat and prod env from local path.

![alt text](<26a wrote an ansible playbook to Setup Kubernetes Namespaces and Secrets for Web Deployment,  create Docker registry secret for dev, uat and prod  namespace and  Deployment of Helm chart for dev, uat and prod  env from local path.png>)

![alt text](<26b wrote an ansible playbook to Setup Kubernetes Namespaces and Secrets for Web Deployment,  create Docker registry secret for dev, uat and prod  namespace and  Deployment of Helm chart for dev, uat and prod  env from local path.png>)

![alt text](<26c wrote an ansible playbook to Setup Kubernetes Namespaces and Secrets for Web Deployment,  create Docker registry secret for dev, uat and prod  namespace and  Deployment of Helm chart for dev, uat and prod  env from local path.png>)

Ran the ansible playbook succesfully

![alt text](<27. Ran the ansible playbook succesfully-1.png>)

Ran the kubectl get pods, kubectl get svc and kubectl get secret to confirm the playbook is working perfectly well

Opened the urls for each environment in their respctive namespaces i.e. dev, uat and prod on the browser

![alt text](<29. dev page.png>)

![alt text](<30. uat page.png>) 

![alt text](<31. prod page.png>)