# Razorpay integration with Test cases


## Overview
Simple Django app which allow user to pay as per their need using Razorpay payment gateway.




## Table of Contents

1. [Features](#features)

2. [Prerequisites](#prerequisites)
   - [Benefits](#benefits)

3. [Installation](#installation)
   - [Demo Video](#demo-video)

4. [Project Structure](#project-structure)
   - [Sequence Diagram for Razorpay Integration in My Project](#sequence-diagram-for-razorpay-integration-in-my-project)
   - [Sequence Diagram for Razorpay Integration Test Cases in My Project](#sequence-diagram-for-razorpay-integration-test-cases-in-my-project)
   - [Test Case](#test-case)
   - [Steps to Get Client ID, Live Secret Key from Razorpay](#steps-to-get-client-id-live-secret-key-from-razorpay)


## Features

List the key features and functionalities of your project.

- Feature 1: User can pay using multiple payment method.
- Feature 2: If the payment fails or get success the user will get a pop up message.
- Feature 3: Description about the creator.
- Feature 4 : Proper data logging in database
- Feature 5 : 2 Test cases for unit testing of the product. 

## Prerequisites



- python == 3.9
- Django==4.2.6
- razorpay razorpay==1.4.1
  
  
#### Benefits:
1. Easily add payments to your website or app
2. Access a wide range of payment solutions and services

3. Manage and track money movements to vendors
4. Get reliable fraud prevention and security

## Installation


Provide step-by-step installation instructions for your project.

1. Clone the repository: `git clone `
2. Change to the project directory: `cd payment_gateway    `
3. Install dependencies: `pip install -r requirements.txt`
4. Paste your razorpay auth keys whether in settings.py file or .env file 
5. Run following command python manage.py makemigrations , python manage.py migrate , python manage.py createsuperuser, python manage.py runserver

 
#####  Demo video  
https://drive.google.com/file/d/1hr773CTBEjI_3YfAd1Db2_r7Vak9lwJ3/view?usp=sharing

## Project structure
![Screenshot (3)](https://github.com/krsatyam99/razorpay_pg/assets/103446420/6068bf03-1e8a-439e-ae74-887dd04bee65)



### Sequence Diagram for razorpay integration in my project.
![Razorpay Integration](https://github.com/krsatyam99/razorpay_pg/assets/103446420/e0587210-009c-426e-8991-b7e6c2024b71)
### Sequence Diagram for razorpay integration testcases in my project.
![Razorpay Test case](https://github.com/krsatyam99/razorpay_pg/assets/103446420/bccdeb82-d05c-406d-a862-5df961b5c59a)
### Test case 


![Screenshot (2)](https://github.com/krsatyam99/razorpay_pg/assets/103446420/230172f4-14e8-43e5-8115-d1002c318960)

#### Note:- 
For acessing the PG in razorpay you need the secret key and Id .
Here, I'm integrating in test mode.
##### Steps to get Client Id, Live Secret Key from Razorpay :
Step 1: Go to Razorpay.

Step 2: If you have a Razorpay account , login, else Signup.

Step 3: Click on Settings.
  
![a33](https://github.com/krsatyam99/Plotly-and-Razorpay/assets/103446420/256baf0a-531e-4d5b-8392-2696e88f0e57)

Step 4: Click on API Keys


![a34](https://github.com/krsatyam99/Plotly-and-Razorpay/assets/103446420/01122554-c747-444c-b7e8-3214477b43bd)

Step 5: Click on Generate Test Key
![a35](https://github.com/krsatyam99/Plotly-and-Razorpay/assets/103446420/aebf5465-3ea1-4e51-bd09-3a3990c1432e)

Step 6: The Client Id and Secret Key will appear. Copy these keys and click on OK or you can download in your local PC.

![a36](https://github.com/krsatyam99/Plotly-and-Razorpay/assets/103446420/4e34bac7-5e7d-4a37-8bdc-146e178a966b)








