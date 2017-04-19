 Personal blog using Django & Heroku 

## Requirements

- iOS 9.0+ / watchOS 2.0+
- Xcode 7.3+

## Installation
- Create a virtual environment for a project: :  
    cd /personal_website/
    python -m venv myvenv

- Start your virtual environment by running: 
    win : myvenv\Scripts\activate
    osx : source\myvenv\bin\activate

- Installing Django:
    pip install --upgrade pip
    pip install django~=1.10.0

- Database Migrate :
    python manage.py migrate


- Heroku Deployment :
    pip install django-toolbelt
    heroku create 'heroku_name'

- git:
    remote list: git remote -v
    delete remote git : git remote rm  'git_name'

