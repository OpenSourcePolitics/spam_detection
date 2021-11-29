PWD=$(shell pwd)
PORT := 8080
TAG := spam_detection:latest

build:
	docker build -t python-mapping . --compress --tag $(TAG)

run:
	docker run -it -e PORT=$(PORT) -p $(PORT):$(PORT) --rm $(TAG)

start:
	@make build
	@make run

bash:
	docker run -it --rm $(TAG) /bin/bash