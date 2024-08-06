CONTAINER_BUILD_ENGINE ?= docker
CONTAINER_BUILD_ENGINE_OPT ?="--platform linux/amd64"

image-build:
	${CONTAINER_BUILD_ENGINE} build -f Containerfile . --tag quay.io/rhcloudperfscale/galaxy-ng-locust:ansible2.9 --build-arg ee_container=registry.redhat.io/ansible-automation-platform-22/ee-29-rhel8   ${CONTAINER_BUILD_ENGINE_OPT}
	${CONTAINER_BUILD_ENGINE} build -f Containerfile . --tag quay.io/rhcloudperfscale/galaxy-ng-locust:ansible2.13 --build-arg ee_container=registry.redhat.io/ansible-automation-platform-22/ee-supported-rhel8  ${CONTAINER_BUILD_ENGINE_OPT}
	${CONTAINER_BUILD_ENGINE} build -f Containerfile . --tag quay.io/rhcloudperfscale/galaxy-ng-locust:ansible2.14 --build-arg ee_container=registry.redhat.io/ansible-automation-platform-23/ee-supported-rhel8   ${CONTAINER_BUILD_ENGINE_OPT}

image-push:
	${CONTAINER_BUILD_ENGINE} push quay.io/rhcloudperfscale/galaxy-ng-locust:ansible2.14
	${CONTAINER_BUILD_ENGINE} push quay.io/rhcloudperfscale/galaxy-ng-locust:ansible2.9
	${CONTAINER_BUILD_ENGINE} push quay.io/rhcloudperfscale/galaxy-ng-locust:ansible2.13
