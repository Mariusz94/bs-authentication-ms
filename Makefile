# Set git local user
git_config:
	git config user.name "Mariusz94"
	git config user.email "lyszczarz.mariusz@gmail.com"

# Create virtual environment
create_venv:
	python3.8 -m venv venv
	source ./venv/bin/activate && \
	pip install -r ./app/requirements.txt && \
	pip install pytest && \
	pip install -U sphinx && \
	pip install sphinx-rtd-theme


# Make docs with Sphinx
doc:
	make -C ./docs doc

# Make tests
test:
	pytest -s -vv tests/functional_tests/grpc_tests.py

# Method to remove folders
# Usage: make rm DIR=ec-files-proto
rm:
ifeq ($(OS), Windows_NT)
	rmdir /s /q $(DIR)
else
	rm -rf $(DIR)
endif


###########################################
# Proto files
###########################################

# Generate proto messages
gen_proto: clone_structure_project_generator proto_generate
	make rm DIR=structure_project_generator
	@ECHO Generating proto message ended with SUCCESS

# Cloning repository 'structure_project_generator'
clone_structure_project_generator:
	@ECHO Cloning repository 'structure_project_generator'
	git clone --branch dev https://github.com/Mariusz94/structure_project_generator.git

# Method to generate proto messages
proto_generate:
	@ECHO ---------------- Generate proto files ----------------
	make gen_spec_proto PROTO_FILE=./structure_project_generator/grpc MESSAGE_NAME=default_msg/default.proto
	make gen_spec_proto PROTO_FILE=./structure_project_generator/grpc MESSAGE_NAME=foo_msg/foo.proto

# Method to generate specific proto message
# Usage: make gen_spec_proto PROTO_FILE=./structure_project_generator/grpc MESSAGE_NAME=default_msg/default.proto
gen_spec_proto:
	@ECHO ---------------- Generate proto file $(MESSAGE_NAME) ----------------

	python -m grpc_tools.protoc -I$(PROTO_FILE) --python_out=./app/grpc_file --pyi_out=./app/grpc_file --grpc_python_out=./app/grpc_file $(PROTO_FILE)/$(MESSAGE_NAME)
	cp $(PROTO_FILE)/$(MESSAGE_NAME) ./app/grpc_file/$(MESSAGE_NAME)
	
	python -m grpc_tools.protoc -I$(PROTO_FILE) --python_out=./tests/ --pyi_out=./tests/ --grpc_python_out=./tests/ $(PROTO_FILE)/$(MESSAGE_NAME)
	cp $(PROTO_FILE)/$(MESSAGE_NAME) ./tests/$(MESSAGE_NAME)

