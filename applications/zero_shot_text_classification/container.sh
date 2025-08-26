#!/usr/bin/env bash
CONTAINER_NAME=zhangweili_cam_work_order
IMAGE_NAME=docker.cipsup.cn/dengziliang/usm-test6.0:latest

docker stop ${CONTAINER_NAME}
docker rm ${CONTAINER_NAME}


docker run \
    --gpus all \
    -d -it --name ${CONTAINER_NAME} \
    --volume ${PWD}/:/home/weili/zero_shot_text_classification \
    -v ${PWD}/models/utc-base:/root/.paddlenlp/models/utc-base \
    --workdir /home/weili/zero_shot_text_classification ${IMAGE_NAME} \
    /bin/bash