IMAGE_NAME = healthdb-backend
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

docker-run:
	@docker run \
	-e FLASK_APP=src/debug_server.py \
	-e FLASK_DEBUG=1 \
		-e DATABASE_FILE_PATH=/database/database.db \
		-e HEALTHDB_SECRET_KEY=${HEALTHDB_SECRET_KEY} \
	  -e HEALTHDB_SECURITY_PASSWORD_SALT=${HEALTHDB_SECURITY_PASSWORD_SALT} \
		-e LOCAL_USER_ID=`id -u ${USER}` \
		-v ${CORE}/backend/src:/src \
		-v ${CORE}/backend/database.db:/database/database.db \
		-p 5000:5000 \
		${OPTIONS} \
		${IMAGE_NAME}:latest \
		${COMMAND}

debug:
	make OPTIONS='-it' COMMAND='bash' docker-run
run:
	make COMMAND='/venv/bin/python -m flask run --host=0.0.0.0' docker-run
