# D00Movenok HW2

## Description

All tasks were solved.

### Technologies stack

- backend: python3.10, FastAPI, MongoDB, Motor, SocketIO
- frontend: VueJS 3, TypeScript, Vuetify, Pinia, Axios, SocketIO-client

### Deploy

```bash
docker compose up --build -d
```

Now the application is listening on `0.0.0.0:5000`.

### Screenshots

![login page](screenshots/login.png)
![profile page](screenshots/profile.png)

## Task

In this home work, you will implement authentication feature for your web application with data stored in database

### Basic part: Implement authentication feature

- [X] 1.1 Listen on localhost:5000
- [X] 1.2 Render authentication form at http://localhost:5000/
- [X] 1.3 Redirect user to profile page if successfully authenticated
- [X] 1.4 Show profile page for authenticated user only at http://localhost:5000/profile
- [X] 1.5 User name and password are stored in Mongodb

### Advanced part

- [X] 2.1 Implement feature that allows users to create new account, profile will be shown with data respected to each account.
- [X] 2.2 Implement password hashing, logout and password change features
- [X] 2.3 Allow users to update profile picture (new user will have a default profile picture)
- [X] 2.4 Allow users to update profile information

### Challenging part

- [X] Implement notification, an active user will receive notification when a new account is created.

* Upload the code to a separate GitHub repository (https://github.com/itmo-wad/username-hw2)
* Describe what you implemented in README.md
* Submit the link to your work to this assignment
