# Insurance Fraud Detection Using IBM WATSON STUDIO 

## Introduction

The objective of this project is to identify whether policy application deserved approval or needed to be denied.  
**Steps:**
1. A customer files a claim.
2. Collect relevant information about the incident. 
3. Input this information into the system.
4. AI works behind the scenes to help determine claim eligibility. 

We worked with some auto insurance data to demonstrate how we can build a predictive model that predicts if an insurance claim is fraudulent or not.
Generating insights like predicted fraud count by insured hobbies.

**Steps to build a Machine Learning Model:**
1. Data Import
2. Data Exploration
3. Data Processing
4. Create Model
5. Selecting Model and deployment
6. Use the API for application building


### Main features

* Simple and ready to use application with two buttons for randomizing and solving the puzzle

* User can also solve the puzzle manually using mouse clicks

* Bootstrap static files included

* Procfile for easy deployments

* Separated requirements files
      
### Getting Started

This assumes that `python` is linked to valid installation of python and that `pip` is installed and `pip`is valid
for installing python packages.

Installing, creating and activating virtualenv

    $ pip install virtualenv
    $ python -m virtualenv venv
    $ source venv/bin/activate


Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

    $ pip install -r requirements.txt
     
#### Sample .env file

.env
```
IBM_MODEL_API_KEY="ibm secret api key"
```
      
After that just install the local dependencies start the development server:

    $ python manage.py collectstatic
    $ python manage.py runserver

Navigate to the default port on your localhost to see the web application:

```djangourlpath
http://127.0.0.1:8000/home
```

## 📸 ScreenShots
![sample output](/screenshots/arch_sys.png)
![sample output](/screenshots/model_training.png)
![sample output](/screenshots/after%20model%20training.png)
![sample output](/screenshots/1.png)
![sample output](/screenshots/2.png)
![sample output](/screenshots/3.png)
![sample output](/screenshots/4.png)

### Execution
![sample result](/screenshots/result.png)
