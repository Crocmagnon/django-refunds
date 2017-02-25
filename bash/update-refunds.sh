#!/bin/bash
set -e
BASE_IMAGE="refunds"
REGISTRY="crocmagnon"
IMAGE="$REGISTRY/$BASE_IMAGE"
CID=$(docker ps | grep $IMAGE | awk '{print $1}')
docker pull $IMAGE

for im in $CID
do
    LATEST=`docker inspect --format "{{.Id}}" $IMAGE`
    RUNNING=`docker inspect --format "{{.Image}}" $im`
    NAME=`docker inspect --format '{{.Name}}' $im | sed "s/\///g"`
    echo "Latest:" $LATEST
    echo "Running:" $RUNNING
    if [ "$RUNNING" != "$LATEST" ];then
        echo "upgrading $NAME"
        docker stop $NAME
        docker rm -f $NAME
        docker run \
            -v /opt/conf/www/$NAME:/app/staticfiles \
            --name $NAME \
            --env-file /opt/conf/environments/$NAME.env \
            --restart always \
            --net web \
            -d $IMAGE
    else
        echo "$NAME up to date"
    fi
done
