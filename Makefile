# Variables                                                                                                                                                   
CONTAINER_NAME:=haproxy
UWSGI_FILE:=/opt/api.ini
CHDIR:=/opt

help: ; @ \
	clear; \
	echo ""; \
	echo "Usage instructions:"; \
	echo ""; \
	echo 'make build: \tCreate new development environment'; \
	echo 'make start: \tStart development environment previously created'; \
	echo 'make stop: \tStop development environment'; \
	echo 'make status: \tShow development environment'; \
	echo 'make restart: \tRestart development environment'; \
	echo 'make logs \tShow development environment logs'; \
	echo 'make clean \tClean dangling volume and images from docker'; \
	echo "make help: \tHow to use make command";\
	echo ""; 

build: ; @\
	clear; \
	echo "[Building Development Environment...]"; \
	echo "";\
	docker-compose down ; \
	docker-compose up --build --remove-orphans -d ; \
	docker exec ${CONTAINER_NAME} uwsgi ${UWSGI_FILE} --chdir ${CHDIR} 

start: ; @\
	clear; \
	echo "[Starting Development Environment...]"; \
	echo ""; \
	docker-compose up -d; \
	docker exec ${CONTAINER_NAME} uwsgi ${UWSGI_FILE} --chdir ${CHDIR}

stop: ; @\
	clear; \
	echo "[Stopping Development Environment...]"; \
	echo "";\
	docker-compose down

status: ; @\
	clear; \
	echo "[Status...]"; \
	echo "";\
	docker-compose ps

clean: ; @\
	clear; \
	echo "[Cleaning Dangling images...]"; \
	echo "";\
	docker rmi -f `docker images -q -f dangling=true`; \
	echo "";\
	echo "[Cleaning Dangling volumes...]"; \
	echo "";\
	docker volume rm `docker volume ls -q -f dangling=true`

restart: stop start

logs: ; @\
	clear; \
	echo "[Generating environment logs...]"; \
	echo "";\
	docker-compose logs
