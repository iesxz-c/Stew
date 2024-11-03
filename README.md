# Stew Backend - Flask API

The backend for the Stew collaborative study application is built using Flask. This API handles data management, authentication, and communication between the frontend and the database.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [API Documentation](#api-documentation)
- [Database](#database)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Stew backend serves as the foundation for the Stew application, providing essential functionalities such as user authentication, data storage, real-time communication, task management, and a doubt resolution feature using generative AI.

## Features

### User Authentication
- **JWT-Based Authentication**: Secure user registration and login, ensuring that only authorized users can access protected resources.

### Timetable Management
- Create, read, update, and delete study timetables, allowing users to manage their study schedules effectively.

### Group Management
- Create and manage study groups, including functionalities for adding members, sending messages, and sharing files.

### Task Management
- Create, read, update, complete, and delete tasks.
- View scores related to task completion.

### Doubt Resolution
- Ask questions and receive answers generated by a generative AI model.
- Store and retrieve the history of questions and answers.

### Flashcards
- Create, update, and delete flashcards to help users reinforce their learning and improve retention.

### Data Visualization
- Provide endpoints to fetch user progress and scores, enabling the frontend to visualize data effectively.

## Technologies Used

- **Backend Framework**: Flask
- **Database**: SQLite for local development (can be extended to other databases like PostgreSQL for production)
- **Authentication**: JSON Web Tokens (JWT)
- **Real-time Communication**: Flask-SocketIO (if applicable)
- **Data Validation**: Marshmallow or Flask-SQLAlchemy for data serialization and validation
- **Generative AI**: Google Gemini for generating answers to doubts

## API Documentation

### Base URL
The base URL for the API is:
```
http://localhost:5000
```

### Endpoints

#### User Authentication
- `POST /register`: Register a new user
- `POST /login`: Authenticate an existing user and receive a JWT

#### Timetable Management
- `GET /timetable`: Retrieve user timetables
- `POST /timetable`: Create a new timetable
- `PUT /timetable/<id>`: Update a timetable by ID
- `DELETE /timetable/<id>`: Delete a timetable by ID

#### Group Management
- `POST /groups`: Create a new study group
- `GET /groups`: Retrieve all groups for a user
- `POST /groups/<id>/members`: Add a member to a group
- `GET /groups/<id>`: Retrieve a specific group and its members
- `DELETE /groups/<id>`: Delete a group

#### Task Management
- `POST /tasks`: Create a new task
- `GET /tasks`: Retrieve all tasks for the current user
- `POST /tasks/<int:task_id>/complete`: Mark a task as completed
- `DELETE /tasks/<int:task_id>`: Delete a task
- `GET /tasks/scores`: Get total tasks, completed tasks, and total score

#### Doubt Resolution
- `POST /ask`: Ask a question and receive an answer
- `GET /history`: Retrieve the history of questions and answers

### Real-Time Group Chat

The Flask server runs with Socket.IO support to manage live chat events. When a user sends a message, the server emits it to all connected clients in the same group room, ensuring everyone receives the message simultaneously. Key functions include:

- **User authentication**: JWT tokens are validated before users can join chat rooms.
- **Message broadcasting**: Messages are broadcasted within each group chat room.
- **Room management**: Users are added to or removed from rooms dynamically based on their activity.

This setup ensures that all users within a group chat experience seamless, real-time communication.

## Database

### Database Management with SQLAlchemy

**SQLAlchemy** is used in Stew as an ORM (Object Relational Mapper) to interact with the database in a more Pythonic way, abstracting away complex SQL queries. It allows us to define database models as Python classes, which makes it easier to read and maintain our code. Each model represents a table in the database, with class attributes corresponding to columns. For instance, in Stew, models like `Task`, `User`, and `Doubt` define various fields like `title`, `description`, and `completed`, along with relationships between models. With SQLAlchemy, we can handle all CRUD operations—Create, Read, Update, Delete—on these models effortlessly, using Python.

### Database Version Control with Flask-Migrate

**Flask-Migrate** provides version control for database migrations by leveraging **Alembic**, a database migration tool for SQLAlchemy. As Stew evolves, its database schema might need updates, like adding new tables or modifying existing columns. Flask-Migrate helps us manage these schema changes smoothly without losing data. When we modify our model classes, we can use Flask-Migrate to generate migration scripts. These scripts record the necessary SQL commands to update the database schema, allowing us to:

- **Upgrade**: Apply the latest changes to the database.
- **Downgrade**: Revert to an earlier database schema version, if needed.

Using Flask-Migrate ensures that the database schema stays synchronized with the application’s codebase, making it easier to track and apply changes across different environments, like development, staging, and production.

### Response Format
Responses are typically returned in JSON format, with appropriate HTTP status codes.

### Requirements
The following are the key dependencies used in the Stew backend application:

**Flask**: Core web framework for building the backend API.

**Flask-JWT-Extended**: Adds JWT (JSON Web Token) authentication for securing API endpoints.

**Flask-SocketIO**: Enables real-time, bi-directional communication for features like group chat.

**Flask-SQLAlchemy**: ORM for database interactions, making it easier to manage data models.

**Flask-Migrate**: Handles database migrations and schema changes with Alembic.

**SQLAlchemy**: Core SQL toolkit and ORM for database management.

**APScheduler**: Adds scheduling capabilities, useful for tasks like sending reminders or notifications.

**google-generativeai**: Enables integration with Google’s generative AI for features like AI-assisted doubt solving.


## Installation

To set up the Stew backend, follow these steps:

1. **Clone the Repository**:
   Open your terminal and run the following command to clone the repository:
   ```bash
   git clone https://github.com/iesxz-c/Stew-Server.git
   ```

2. **Navigate to the Backend Directory**:
   Change your current working directory to the backend folder:
   ```bash
   cd Stew/backend
   ```

3. **Create a Virtual Environment** (optional but recommended):
   It's a good practice to use a virtual environment to manage your dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install the Dependencies**:
   Install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**:
   Start the Flask development server:
   ```bash
   flask run
   ```

6. **Open Your Browser**:
   The API will be accessible at `http://localhost:5000`.

## Usage

Once the backend is running, you can interact with the API using tools like Postman or cURL. Make sure to follow the API documentation for the correct endpoints and payloads.

## Contributing

We welcome contributions to the Stew backend! If you'd like to contribute, please follow these steps:

1. **Fork the Repository**: Click the "Fork" button in the top right corner of the repository page.
   
2. **Clone Your Fork**: Clone your forked repository to your local machine:
   ```bash
   git clone https://github.com/your-username/Stew-Server.git
   ```

3. **Create a New Branch**: Always create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```

4. **Make Changes**: Implement your changes and commit them with a descriptive message:
   ```bash
   git commit -m "Description of the changes made"
   ```

5. **Push Changes**: Push your branch to your forked repository:
   ```bash
   git push origin feature-name
   ```

6. **Create a Pull Request**: Go to the original repository and click on the "Pull Requests" tab to submit your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Frontend Link

For the frontend of the Stew application, visit: [Stew Client](https://github.com/iesxz-c/Stew-Client)

---

Thank you for checking out the Stew backend! We hope it provides a solid foundation for your collaborative study needs. If you have any questions or feedback, feel free to reach out.
