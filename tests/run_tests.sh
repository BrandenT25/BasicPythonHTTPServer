#!/usr/bin/bash
set -e
venv_path="venv/bin"
source "$venv_path/activate"


 
nohup python BasicPythonHttpServer.py > server.log 2>&1 &
PID=$!
sleep 1
cd tests/
pytest test_server.py
sleep 1
kill $PID
deactivate


