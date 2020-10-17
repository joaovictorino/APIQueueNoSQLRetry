# General

![Components](https://github.com/joaovictorino/APIQueueNoSQLRetry/blob/master/documentation/api.jpg?raw=true)

# How to run

1. Create queue RabbitMQ on CloudAMQP
2. Create database on MongoDB Atlas
3. Update connection string of RabbitMq and MongoDB on config.ini
4. Run service stock on ./resource/serverStock.py (python ./resource/serverStock.py)
5. Run API on app.py (python app.py)
6. Run worker on worker.py (python worker.py)
7. Import Postman collection on ./postman/API.postman_collection.json
8. Update host address on postman and execute
