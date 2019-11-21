
build:
	@echo "Start building tests..."
	docker-compose build
run:
	@echo "Start running tests..."
	docker-compose run --rm python
	@echo "All TESTS DONE"
clean:
	@echo "Start cleaning tests..."
	sudo find . -name \*.pyc -delete
