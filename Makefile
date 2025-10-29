NOW_DATE := $(shell date -u +'%Y-%m-%dT%H:%M:%SZ')

SCRIPTS = deploy/env-generate.py deploy/run_container.sh

.SECONDARY:

.DEFAULT_GOAL := fix-permissions

test:
	cd src && ./manage.py test --keepdb

test-fast:
	cd src && ./manage.py test --keepdb --parallel 4

lint:
	cd src && flake8 --config=.flake8-ci jt/ 2>/dev/null

lint-strict:
	cd src && flake8 --config=.flake8 jt/ 2>/dev/null

check:	lint test

docker-build:	Dockerfile
	@JT_VERSION=$$(cat TT_VERSION); \
	docker build \
		--label "name=jt" \
		--label "version=$$JT_VERSION" \
		--label "build-date=$(NOW_DATE)" \
		--tag jt:$$TT_VERSION \
		--tag jt:latest .

docker-run:	.private/env/local.dev Dockerfile fix-permissions
	./deploy/run_container.sh -bg

docker-run-fg:	.private/env/local.dev Dockerfile fix-permissions
	./deploy/run_container.sh

docker-stop:	
	docker stop jt

env-build:	.private/env/local.dev fix-permissions
	./deploy/env-generate.py --env-name local

env-build-dev:	.private/env/development.sh fix-permissions
	./deploy/env-generate.py --env-name development

.private/env/local.dev:

.private/env/development.sh:

.PHONY:	fix-permissions

fix-permissions:
	@echo "Setting execute permissions for $(SCRIPTS)"
	chmod +x $(SCRIPTS)


