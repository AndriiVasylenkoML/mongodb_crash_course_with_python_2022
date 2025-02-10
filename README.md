# MongoDB Crash Course With Python 2022
MongoDB is a user-friendly and popular document-oriented database that allows users to easily manage data in collections of documents. 
---

1. Start MongoDB.
You can start the mongod process by issuing the following command:
```
sudo systemctl start mongod
```
If you receive an error similar to the following when starting mongod:

Failed to start mongod.service: Unit mongod.service not found.

Run the following command first:
```
sudo systemctl daemon-reload
```
Then run the start command above again.

2. Verify that MongoDB has started successfully.
sudo systemctl status mongod

You can optionally ensure that MongoDB will start following a system reboot by issuing the following command:
```
sudo systemctl enable mongod
```
3. Stop MongoDB.
As needed, you can stop the mongod process by issuing the following command:
```
sudo systemctl stop mongod
```
4. Restart MongoDB.
You can restart the mongod process by issuing the following command:
```
sudo systemctl restart mongod
```
You can follow the state of the process for errors or important messages by watching the output in the /var/log/mongodb/mongod.log file.

5. Begin using MongoDB.
Start a mongosh session on the same host machine as the mongod. You can run mongosh without any command-line options to connect to a mongod that is running on your localhost with default port 27017.
```
mongosh
```
For more information on connecting using mongosh, such as to connect to a mongod instance running on a different host and/or port, see the mongosh documentation.

To help you start using MongoDB, MongoDB provides Getting Started Guides in various driver editions. For the driver documentation, see Start Developing with MongoDB.


Sources:
1. MongoDB Crash Course With Python 2022. YouTube: https://youtu.be/qWYx5neOh2s?si=RuQ0WUIEneR5FvUu