<h4>This repository contains functions for the task management application</h4>

## 1. Introduction
### Overview
The application will allow team members with appropriate permission to create, update, and delete tasks on a to-do list

### Purpose
This documentation serves as a guide for developers and administrators to understand, integrate, and use the MO-fail data extractor script.

## 2. Getting Started
### Prerequisites
Before using this Application, make sure you have the following:
- python 3.10.5
- pip 24

### Installation
Follow these steps to install the Application:
- Download the latest release from the [GitHub repository] (git@github.com:vinay60413/project_manager.git).
- run `Scripts\activate` in windows and other operating system
- run `sh Scripts\activate.sh` in ubuntu
- run `python -m pip install -r .\requirements.txt`
- run `python manage.py createsuperuser` This will prompts for superuser details
- run `python manage.py makemigrations` 
- run `python manage.py migrate` 
- run `python manage.py runserver`


## 3. Configuration

Edit the `project_manager/settings.py` file to set up the Application
Before running the script, change the below variables <br>
`DEBUG = False` <br>
In templates/tasks/task_detail.html replce http://127.0.0.1:8000/ with the particular domain URL

## 4. Usage

- [Endpoints](#endpoints) <br/>
  These endpoints allow you to handle project manager app.
  - `List all projects` [/projects/](#projects)<br/>
  - `Add a project` [/projects/add_project/](#projects)<br/>
  - `Details of a particular project` [/projects/<int:project_id>/](#projects/1)<br/>
  - `Add a task` [/projects/project/<int:project_id>/add_task/](#projects/1)<br/>
  - `Task detail` [/projects/task/<int:task_id>/](#projects)<br/>
  - `Remove Task` [/projects/task/<int:task_id>/complete/](#projects)<br/>
  - `chats` [/projects/chat/](#projects)<br/>



## 5. Recent changes made in Repository are: 
<ol>
    <li>Initial setup completed.</li>
</ol>
