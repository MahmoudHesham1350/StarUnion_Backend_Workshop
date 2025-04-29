# Star Union Backend Workshop

Welcome to the official repository for the Star Union Backend Workshop online sessions! This repository contains all the materials, code examples, and resources used during our 11-week backend development workshop.

## About the Workshop

This 11-week workshop covers fundamental and advanced concepts in backend development. Each week focuses on specific topics, with materials organized in weekly branches.

## Repository Structure

The workshop content is organized by weeks. Each week's materials are stored in a separate branch named `week1`, `week2`, etc., up to `week11`.

## How to Access Workshop Materials

### Cloning the Repository

To get started, clone this repository to your local machine:

```bash
git clone https://github.com/MahmoudHesham1350/StarUnion_Backend_Workshop.git
cd StarUnion_Backend_Workshop
```

### Accessing Weekly Materials

To access materials for a specific week, switch to the corresponding branch:

```bash
# To access Week 1 materials
git checkout week1

# To access Week 2 materials
git checkout week2

# And so on...
```

### Listing All Available Branches

To see all available week branches:

```bash
git branch -r
```

## Material Updates

New materials will be uploaded to the respective week's branch after each online session. To get the latest updates for the current week:

```bash
git pull origin week<number>
```

## Weekly Content Overview

- **Week 1**: Python Basics I
  - Python installation and setup (Pyenv, virtual environments)
  - Variables and data types (strings, integers, floats, booleans)
  - Basic operators (arithmetic, comparison, logical)
  - Input/output (input(), print(), file handling basics)
  - Practical exercises: Build a simple calculator program and a program to read/write to a text file

- **Week 2**: Python Basics II
  - Control structures (if, else, elif, nested conditions)
  - Loops (for, while, break, continue)
  - Lists, tuples, and dictionaries (methods, slicing, iteration)
  - Practical exercises: Build a number guessing game and a program to manage a list of tasks

- **Week 3**: Python Functions & OOP
  - Functions (definition, parameters, return values, scope)
  - Lambda functions and higher-order functions
  - Classes and objects (attributes, methods, constructors)
  - Inheritance and polymorphism
  - Practical exercises: Create a class hierarchy for a library system (e.g., Book, User, Library)

- **Week 4**: Database Fundamentals
  - Introduction to relational databases (SQLite, MySQL, PostgreSQL)
  - SQL basics (CREATE, INSERT, SELECT, WHERE)
  - UPDATE and DELETE operations
  - Primary keys, foreign keys, and relationships (one-to-many, many-to-many)
  - Practical exercises: Create a database for a blog system (users, posts, comments)

- **Week 5**: Django Basics
  - Django installation and setup
  - Project structure (settings.py, urls.py, wsgi.py)
  - URLs and views (routing, basic view functions)
  - Templates basics (rendering HTML, passing context)
  - Practical exercises: Create a simple Django project with a homepage and about page

- **Week 6**: Django Models
  - Models definition (fields, field types, relationships)
  - Migrations (makemigrations, migrate)
  - QuerySet API (filtering, updating, deleting)
  - Admin interface (registering models, customizing admin)
  - Practical exercises: Create a blog application with models for Post, Comment, and Author

- **Week 7**: Django Views and Forms
  - Function-based views (request/response cycle, handling forms)
  - Class-based views (ListView, DetailView, CreateView)
  - Forms processing (Django forms, validation, CSRF)
  - Practical exercises: Build a CRUD application for managing tasks or blog posts

- **Week 8**: Django REST Framework (DRF) Basics
  - What is REST? (Principles, HTTP methods, status codes)
  - API endpoints design (RESTful principles, versioning)
  - Setting up Django REST Framework
  - Serializers (ModelSerializer, custom serializers)
  - Basic API views (APIView, GenericAPIView)
  - Practical exercises: Create a simple API for the blog application (list posts, create posts)

- **Week 9**: Advanced Django REST Framework
  - Authentication (TokenAuthentication, SessionAuthentication)
  - Permissions (IsAuthenticated, IsAdminUser, custom permissions)
  - Viewsets and routers (ModelViewSet, DefaultRouter)
  - Pagination and filtering
  - Practical exercises: Add authentication and permissions to the blog API

- **Week 10**: Django Authentication and Security
  - User authentication (login, logout, registration)
  - Password management and hashing
  - Permissions and groups
  - Security considerations (CORS, CSRF, SQL injection)
  - Practical exercises: Build a user management system with registration and login

- **Week 11**: Final Project Backend
  - Deployment basics (Docker, Gunicorn)
  - Caching
  - Scalability and optimization
  - Good and bad response, requests
  - Testing (unit tests, integration tests)
  - Final Project: Build and deploy a complete backend for a web application (e.g., e-commerce, social media, or blog platform)

## Support

If you have any questions or encounter issues with the workshop materials, please reach out to the workshop instructors or create an issue in this repository.

---

Happy coding and we look forward to your participation in the Star Union Backend Workshop!