#!/usr/bin/env bash
CONTAINER_NAME=zhangweili_cam_na_api
IMAGE_NAME=docker.cipsup.cn/dengziliang/usm-test6.0:latest

docker stop ${CONTAINER_NAME}
docker rm ${CONTAINER_NAME}


docker run \
    --gpus all \
    -p 8893:8893 \
    -d --name ${CONTAINER_NAME} \
    -v ${PWD}/:/home/weili/zero_shot_text_classification \
    -v ${PWD}/models/utc-base:/root/.paddlenlp/models/utc-base \
    -e GPU_ID="3" \
    --workdir /home/weili/zero_shot_text_classification ${IMAGE_NAME} \
    sh -c "bash api_na.bash"