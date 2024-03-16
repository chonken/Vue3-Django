<div align="center">
  <img alt="Logo" src="./frontend/src/assets/logo.png">
  <h1>Vue3 + Django</h1>
  <span><a href="README.md">中文</a> | English</span>
</div>

## Introduction

This is a project developed using `Vue3` and `Django`, aiming to experience and showcase the convenience brought by Vue3 and Django in development. It is my first time adopting the front-end and back-end separation development model since graduation, gaining practical insights into CORS, CSRF, using Django's ORM to replace familiar SQL syntax, and mitigating the risks associated with SQL injection.

## Features

#### Backend

###### CRUD

-   **Query**: Retrieve all data from a single table or filter data by fields.
-   **Create**: Add a new data entry.
-   **Update**: Modify an existing data entry.
-   **Delete**: Remove data based on ID.

###### CheckKPI

-   **Query Total Sales**: Retrieve the top 10 entries in the total sales volume leaderboard.
-   **Query Total Revenue**: Retrieve the top 10 entries in the total sales revenue leaderboard.

#### Frontend

-   **Add Customers, Products, Stores**: Add new data entries.
-   **Edit Data**: Modify data for customers, products, or stores.
-   **View Performance**: View total sales and revenue.

## Project Versions

#### Backend

-   **Python**: 3.11.7
-   **Pip**: 23.3.1
-   **Django**: 5.0.3
-   **Django-cors-headers**: 4.3.1
-   **Mssql-django**: 1.4
-   **Pyodbc**: 5.1.0

#### Frontend

-   **Node.js**: 20.11.0
-   **Npm**: 10.2.4
-   **Vue3**: 3.2.13
-   **Bootstrap**: 5.3.2
-   **Axios**: 1.6.7
-   **Font Awesome**: 6.5.1

## Folder Structure

```plaintext
├─ backend              - Backend
│  ├─ DjangoAPI         - Backend Project
│  ├─ CRUD              - CRUD operations app
│  │  └─ models.py      - Model shared by all apps
│  └─ CheckKPI          - App for complex queries
│
└─ frontend             - Frontend
   ├─ public            - Public resources
   └─ src               - Source code
      ├─ assets         - Static resource directory
      ├─ components     - Reusable Vue components
      ├─ views          - Main application page components
      └─ utils          - Common JS utilities
```

## Setting Up Development Environment

```bash
# Clone the project
git clone https://github.com/chonken/Vue3-Django.git

# Navigate to the project directory
cd Vue3-Django
```

#### Start Backend

```bash
# Navigate to the backend
cd backend

# Restore the development environment
pip install -r requirements.txt

# Start the server
python manage.py runserver
```

#### Start Frontend

```bash
# Navigate to the frontend
cd frontend

# Restore the development environment
npm install

# Start the development server
npm run serve
```
