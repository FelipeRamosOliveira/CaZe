#Paths
ANALISYS_PATH = analisys
DEPLOY_PATH = deploy

#Install poetry
poetry:
	python3 -m pip install poetry	

#Install dependencies
$(ANALISYS_PATH)/:
	poetry install

$(DEPLOY_PATH) /:
	poetry install
