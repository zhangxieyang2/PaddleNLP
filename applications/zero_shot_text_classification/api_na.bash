#!/usr/bin/env bash

cd ./deploy/simple_serving
paddlenlp server na_server:app --workers 1 --host 0.0.0.0 --port 8893

