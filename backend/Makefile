.PHONY : test build
shell :
	@poetry shell
test :
	@PYTHONPATH=. python -m pytest -p no:warnings --tb=auto -vv tests

single-test :
	@PYTHONPATH=. python -m pytest -p no:warnings --tb=auto -vv ${FILE}

build:
	@echo "exporting requirements file"
	@poetry export -f requirements.txt --without-hashes --output src/requirements.txt
	@echo "building docker image"
	@docker build -t "liftdb-backend:latest" src
	@echo "hello"

run:
	@docker-compose up
