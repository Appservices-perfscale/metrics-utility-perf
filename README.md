In order for this to work, you will need to do the following steps:

# Build
## Creating the image
```
docker build -f Containerfile . --tag quay.io/rhcloudperfscale/galaxy-ng-locust:ansible2.13 --build-arg ee_container=registry.redhat.io/ansible-automation-platform-22/ee-supported-rhel8 --platform linux/amd64
docker build -f Containerfile . --tag quay.io/rhcloudperfscale/galaxy-ng-locust:ansible2.9 --build-arg ee_container=registry.redhat.io/ansible-automation-platform-22/ee-29-rhel8  --platform linux/amd64
docker build -f Containerfile . --tag quay.io/rhcloudperfscale/galaxy-ng-locust:ansible2.14 --build-arg ee_container=registry.redhat.io/ansible-automation-platform-23/ee-supported-rhel8  --platform linux/amd64
```
## Pushing the image
```
docker push quay.io/rhcloudperfscale/galaxy-ng-locust:ansible2.13
docker push quay.io/rhcloudperfscale/galaxy-ng-locust:ansible2.9
docker push quay.io/rhcloudperfscale/galaxy-ng-locust:ansible2.14
```

# Deploy to openshift/k8s

1. you will need to create a secret yml file with the name rhcloudperfscale-puller-pull-secret
2. replace the TOKEN and URL in k8s/galaxy-config-file.yaml file
5. Make sure you change the image reference in the k8s deployment files to match your images you built and pushed
6. To initially create the deployment, set your namespace with "oc project $NAMESPACE"
7. Then in the k8s folder, run "oc apply -f ."


# Update
1. If you want to update just the ansible.cfg, you can edit the configmap file and delete the deployment and re-apply. The pods need to get redeployed w/ the new config map
2. If you want to update the tests, you need to rebuild the images.
