
# Table of contents
* [Project Info](#project-info)
* [Project Setup](#project-setup)
    * [Tools used](#tools-used)

# Project info
Job Vacancies Tracker is my pet project made with the purpose of simplify job finding for me and other people. Currently supports ONLY hh.ru URLs.

## Tools used
This is a Fullstack web appication. The tools:

### Frontend
- TypeScript
- Vue3 (Composition API)
- Vue-router
- SCSS

### Backend
- Python
- Flask
- Flask-sqlalchemy
- Flask-marshmallow

# Project setup
To run a project, follow these steps:

- Install [NodeJS](https://nodejs.org/en) if you do not have it on your machine.

- Install node dependencies:
   ```bash
   npm install
   # or
   yarn install
   # or
   pnpm install
   ```

- Run the client development server:
  ```bash
  # /client
  npm run dev
  # or
  yarn dev
  # or
  pnpm dev
  ```
  
- Install server dependencies:
   ```bash
   pip install -d flask flask-sqlalchemy flask-marshmallow
   ```

- Run the server development server
   ```bash
   # /server
  python app.py
   # or
  python3 app.py
  ```

- Open [http://localhost:5173](http://localhost:5173) with your browser to see the result.

