#!/usr/bin/env bash

cd ./deploy/simple_serving
paddlenlp server iv_server:app --workers 1 --host 0.0.0.0 --port 8892

