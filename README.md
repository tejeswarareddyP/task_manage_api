Task Management API
This project is a Django-based API for managing tasks. The application uses Django's default SQLite database and is containerized with Docker to streamline setup and deployment.

GitHub Repository
You can find the code in this repository: Task Management API

Getting Started
Prerequisites
Docker: Ensure Docker is installed to run the containers.
Postman: To simplify API testing, it's recommended to use Postman (commands provided below).
Setup and Run Instructions
Clone the repository:

bash
Copy code
git clone https://github.com/tejeswarareddyP/task_manage_api.git
cd task_manage_api
Build and run the Docker container:

bash
Copy code
docker-compose build
docker-compose up
The API will be accessible at http://127.0.0.1:8000/.

Database
This project uses Django's default SQLite (db.sqlite3) database. It is stored in the project's root directory and managed directly by Django.

API Endpoints
The following endpoints allow you to create, read, update, and delete tasks.

Task Model Details
The Task model has the following fields:

title (string, max 255 characters)
description (text)
completed (boolean, defaults to False)
created_at (datetime, automatically added)
updated_at (datetime, automatically updated)
owner (foreign key to the User model)
Postman Collection
Get Access Token (POST)

URL: http://127.0.0.1:8000/api/token/
Body (form-data):
username: Your username
password: Your password
Refresh Access Token (POST)

URL: http://127.0.0.1:8000/api/token/refresh
Body (form-data):
refresh: {{refresh_token}}
Create a Task (POST)

URL: http://127.0.0.1:8000/api/tasks/
Headers:
Authorization: Bearer {{access_token}}
Body (JSON):
json
Copy code
{
  "title": "Sample Task",
  "description": "This is a description of the sample task.",
  "completed": false
}
Get All Tasks (GET)

URL: http://127.0.0.1:8000/api/tasks/
Headers:
Authorization: Bearer {{access_token}}
Get Single Task (GET)

URL: http://127.0.0.1:8000/api/tasks/{id}/
Headers:
Authorization: Bearer {{access_token}}
Update Task (PUT)

URL: http://127.0.0.1:8000/api/tasks/{id}/
Headers:
Authorization: Bearer {{access_token}}
Body (JSON):
json
Copy code
{
  "title": "Updated Task Title",
  "description": "Updated task description",
  "completed": true
}
Delete Task (DELETE)

URL: http://127.0.0.1:8000/api/tasks/{id}/
Headers:
Authorization: Bearer {{access_token}}
Example CURL Commands (Alternative to Postman)
Get Access Token
bash
Copy code
curl -X POST http://127.0.0.1:8000/api/token/ -d "username=your_username&password=your_password"
Refresh Access Token
bash
Copy code
curl -X POST http://127.0.0.1:8000/api/token/refresh -d "refresh={{refresh_token}}"
Create a Task
bash
Copy code
curl -X POST http://127.0.0.1:8000/api/tasks/ -H "Authorization: Bearer {{access_token}}" -H "Content-Type: application/json" -d '{"title": "Sample Task", "description": "This is a description of the sample task.", "completed": false}'
Retrieve All Tasks
bash
Copy code
curl -X GET http://127.0.0.1:8000/api/tasks/ -H "Authorization: Bearer {{access_token}}"
Retrieve Single Task
bash
Copy code
curl -X GET http://127.0.0.1:8000/api/tasks/{id}/ -H "Authorization: Bearer {{access_token}}"
Update Task
bash
Copy code
curl -X PUT http://127.0.0.1:8000/api/tasks/{id}/ -H "Authorization: Bearer {{access_token}}" -H "Content-Type: application/json" -d '{"title": "Updated Task Title", "description": "Updated task description", "completed": true}'
Delete Task
bash
Copy code
curl -X DELETE http://127.0.0.1:8000/api/tasks/{id}/ -H "Authorization: Bearer {{access_token}}"
This setup guide provides instructions for initializing and running the project locally using Docker, along with API testing commands for Postman. Please refer to the repository for code and further documentation
