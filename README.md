# General

![Components](https://github.com/joaovictorino/APIQueueNoSQLRetry/blob/master/documentation/api.jpg?raw=true)

# How to run

1. Create queue RabbitMQ on CloudAMQP
2. Create database on MongoDB Atlas
3. Run service stock on ./resource/serverStock.py (python ./resource/serverStock.py)
4. Run API on app.py (python app.py)
5. Run worker on worker.py (python worker.py)
6. Import Postman collection on ./postman/API.postman_collection.json
7. Update host address on postman and execute