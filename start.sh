#!/bin/bash

poetry install
sudo service docker start
sudo docker-compose -f compose.yaml --env-file config.ini down
#sudo docker system prune
#sudo docker volume remove pppd_db_postgres_data
sudo docker-compose -f compose.yaml --env-file config.ini up -d
echo "done"
