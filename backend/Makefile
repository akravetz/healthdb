.PHONY : test build
shell :
	@poetry shell
test :
	@PYTHONPATH=. python -m pytest -p no:warnings --tb=auto -vv tests

single-test :
	@PYTHONPATH=. python -m pytest -p no:warnings --tb=auto -vv ${FILE}
