#!/usr/bin/bash
set -e
venv_path="../venv/bin/"
source "$venv_path/activate"


cd .. 
nohup python BasicPythonHttpServer.py > server.log 2>&1 &
PID=$!
sleep 1
cd tests/
source ../venv/bin/activate
pytest test_server.py 
kill $PID


