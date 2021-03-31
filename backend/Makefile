IMAGE_NAME = liftdb-backend
.PHONY : test build run
shell :
	@poetry shell
test :
	@PYTHONPATH=. python -m pytest -p no:warnings --tb=auto -vv tests

single-test :
	@PYTHONPATH=. python -m pytest -p no:warnings --tb=auto -vv ${FILE}

seed_db:
	@PYTHONPATH=${CORE}/backend python tools/seeder/seeder.py

build:
	@echo "exporting requirements file"
	@poetry export -f requirements.txt --without-hashes --output src/requirements.txt
	@echo "building docker image"
	@docker build -t "${IMAGE_NAME}:latest" -f Dockerfile src

run:
	@docker run \
	-e FLASK_APP=app.py \
		-e DATABASE_FILE_PATH=/database/database.db \
		-v ${CORE}/backend/src:/src \
		-v ${CORE}/backend/database.db:/database/database.db \
		-p 5000:5000 \
		${IMAGE_NAME}:latest
