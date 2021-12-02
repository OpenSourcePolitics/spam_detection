PWD=$(shell pwd)
PORT := 8080
REGION := fr-par
IMAGE_NAME := spam_detection
VERSION := latest
REGISTRY_ENDPOINT := rg.$(REGION).scw.cloud
REGISTRY_NAMESPACE := osp-internal-tools
REGISTRY_TAG := $(REGISTRY_ENDPOINT)/$(REGISTRY_NAMESPACE)/$(IMAGE_NAME):$(VERSION)
AUTH_TOKEN := dummy

login:
	docker login $(REGISTRY_ENDPOINT) -u userdoesnotmatter -p $(TOKEN)

push:
	docker push $(REGISTRY_TAG)

deploy:
	@make login
	@make push

build:
	docker build -t $(IMAGE_NAME) . --compress --tag $(REGISTRY_TAG)

run:
	docker run -it -e AUTH_TOKEN=$(AUTH_TOKEN) -e PORT=$(PORT) -p $(PORT):$(PORT) --rm $(REGISTRY_TAG)

start:
	@make build
	@make run

bash:
	docker run -it --rm $(TAG) /bin/bash