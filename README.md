### Deploy Dockerized Application to Kubernetes

Ticket-1: Configure a Local Docker Registry on Kubernetes Task: Set up a local Docker registry hosted on a Kubernetes cluster.

Created an eks cluster called ope-cluster on aws

![0 2a create an eks cluster on aws](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/9fe0d9f3-f909-4ce1-a360-c1831be52afd)

Updated the kubeconfig file on the eks cluster on aws to point towards the cluster created.

![0 4a update the kubeconfig file on aws eks cluster](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/8b59856f-e250-4aa1-8132-739f7eed31b2)

Created a secret within the kubernetes cluster called docker-registry-secret to login into the docker registry 

![0 5a create a secret for the docker registry](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/f4bf61da-df68-4f63-bd3a-070c92042475)

Created a deployment and secret manifest file called docker-registry. Ensure the deployment manifest file has imagePullSecrets included in the deployment manifest file. Run the kubectl commands to confirm the secret, run the deployment and serivce manifest files and confirm the pods and services are running succesfully.

![0 6a create a deployment and service manifest files](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/1b647815-6bcc-4a68-9896-314d4cc660c7)

![0 7a deployment and service manifest file command](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/8351faa2-3de3-4c3c-bb10-6ceff3b56457)

Ensured access into the docker registry from my local machine and within the Kubernetes cluster.
![0 9a Ensure you can access the registry from your local machine and within the Kubernetes cluster png](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/12b80a56-9aaa-472e-a34e-ed76b5265826)

Ticket-2: Deploy a Python Web Application to Kubernetes. Accessing the root URL of the application should display a "Hello Kube" message.

Wrote a simple python app whiich displays the  mesage "hello kube"

![0 10 write a simple python app whiich displays the  mesage  hello kube](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/b997e888-48c3-4c7f-9b24-f2e76543ee0b)

Dockerise the python application within the same directory as the python app

![0 11 dockerise the python application within the same directory as the pthon app](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/d46a3051-28c9-4d94-b9bc-9e16d2b62d0a)

Build the dockerised python application and push to the docker registry.

![0 12 build the dockerise web application and push to the docker registry](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/58594518-b349-47f8-a706-26e7689c7b07)

Confirmed the image within the docker registry, ran kubectl get svc, and  used the external IP and port 5000 on the url to confirm the web page is running. Verified access to the application on my local machine's browser.

![0 13a confirm the image within the  docker registry](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/af7359be-1051-4920-adc7-7768932ca12e)

![0 13b Run kubectl get svc, and  use the externalip and port 5000 on the url external IP and the port to confirm the web page is running](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/d7b7df20-72e6-4b9b-b6b2-f6f47f0dcfbc)

![0 13c Verified  access to the application on my local machine's browser](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/4a192868-431e-4019-a0f3-176b34c98793)

Ticket-3: Create a Helm Chart for the Web Application. Develop a Helm chart that can be used to deploy the web application to Kubernetes.

Created an helm chart called 1 by running the command 'helm create 1'

![0 14a create an helm chart called 1](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/83d20f40-83e2-4fea-b9a5-ffd3916445e4)

Created an helm template for deployment, service and values manifest files.

![0 14b created an helm template for deployment file](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/7f2011f2-ac26-4ea6-b283-007c13543129)

![0 15a helm template for service manifest file](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/d0ad3f6f-ae1e-46c8-8dd4-1a83711ba050)

![0 16a values file within helm chart](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/b7f40869-ae98-4822-a97a-8e85497a10e4)


Validated the yaml files produced for the helm chart by running the command 'helm template -f <path of the values.yaml file> <path of the Chart.yaml file>

![0 17a validate the yaml files produced for the helm chart](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/68de137f-57a0-41f4-9580-1241a60ec9f0)

![0 17b validate the yaml files produced for the helm chart](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/2cfff9c1-be2d-49d4-86ad-fb4e78fab422)

Run helm install and confirm it is working  run helm ls and kubectl get pods to confirm the pods are running

![0 20a Run helm install and confirm it is working  run helm ls and kubectl get pods to confirm the pods are running](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/e809202b-79ca-4629-8aee-5feb0f1ead33)


 Ticket-4: Automate Deployment with Ansible. Use Ansible to automate the deployment of the web application.

Modified the application to display "Hello {{ENV}} Kube," where {{ENV}} depends on the environment (dev, uat, prod).


![0 21  modified the application to display  Hello {{ENV}} Kube,  where {{ENV}} depends on the environment (dev, uat, prod)](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/7fb29d9d-ec8a-49a7-b361-de7f492563be)

Rebuilt the modified appplication and pushed to the docker registry, reinstalled the helm chart for the modified application

Modified the deployment manifest file to include env variabe for dev, uat, and prod

![0 24a modify the deployment manifest file to include env parameter for dev, uat and prod](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/291dba99-edf8-44c6-b87a-45d141666fcd)

Updated the helm template for deployment to include env for dev, uat, prod. 

![0 25a update the helm template for deployment to include env  for dev, uat, prod, ](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/b1ce8bf9-17de-4fd1-bd2e-741656540c95)

26a Wrote an ansible playbook to Setup Kubernetes Namespaces and Secrets for Web Deployment,  created Docker registry secret for dev, uat and prod  namespaces and  deployment of helm chart for dev, uat and prod env from local path.

![26a wrote an ansible playbook to Setup Kubernetes Namespaces and Secrets for Web Deployment,  create Docker registry secret for dev, uat and prod  namespace and  Deployment of Helm chart for dev, uat and prod  env from local path](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/553b74f2-61f0-4b5e-8c12-95e73ba90264)

![26b wrote an ansible playbook to Setup Kubernetes Namespaces and Secrets for Web Deployment,  create Docker registry secret for dev, uat and prod  namespace and  Deployment of Helm chart for dev, uat and prod  env from local path](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/04fc6d45-e1bb-4761-b33b-eec517837004)

![26c wrote an ansible playbook to Setup Kubernetes Namespaces and Secrets for Web Deployment,  create Docker registry secret for dev, uat and prod  namespace and  Deployment of Helm chart for dev, uat and prod  env from local path](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/df621db7-142b-4dab-97be-e88d67fac620)


Ran the ansible playbook succesfully

![27  Ran the ansible playbook succesfully](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/cf876c53-659a-4e45-9895-2945271ddfb0)

Ran the kubectl get pods, kubectl get svc and kubectl get secret to confirm the playbook is working perfectly well

![28 Run the kubectl get pods, kubectl get svc and kubectl get secret to confirm the playbook is working perfectly well ](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/ca501229-1c02-4a58-b1ff-4cf5c82d0748)


Opened the urls for each environment in their respctive namespaces i.e. dev, uat and prod on the browser

![29  dev page](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/bd215918-72b3-4397-b302-7c212875afa9)

![30  uat page](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/cd6c4733-49a6-4e53-b06d-58aaa36977c5)

![31  prod page](https://github.com/opeyemiagbadero/Dockerized-Application-to-Kubernetes/assets/79456052/f64a5d7a-52cd-4d9b-913e-d6b6e05f61ae)

