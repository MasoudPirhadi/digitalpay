# DigitalPay

**DigitalPay** is a Django application designed to manage and process installment payments. This system allows businesses and financial institutions to efficiently track and manage installment payments from customers.

## Features

- **Installment Payment Management**: Record, track, and manage customer installment payments.
- **User Management**: Registration and login system for different users with varying access levels.
- **SMS Management**: Send notification SMS messages to users at different stages of the payment process.
- **Admin Dashboard**: A management dashboard for monitoring the status of payments and users.
- **Easy Configuration**: Use of `.env` files for environmental settings and easy configuration.

## Prerequisites

To run this project, you need the following:

- Python 3.10 or higher
- Django 4.2 or higher
- MySQL or SQLite database
- Access to an SMS panel for sending notifications

## Installation and Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/MasoudPirhadi/digitalpay.git
   cd digitalpay
   

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   
4. **Set Up Environmental Settings
Copy the .env-example file to .env and configure the necessary settings, such as database and SMS credentials.**

   ```bash
   cp .env-example .env
   
5. **Run Migrations**
   ```bash
   python manage.py migrate
   
6. **Create Superuser**
   ```bash
   python manage.py createsuperuser

7. **Run the Server**
   ```bash
   python manage.py runserver
   
**Usage
Once the server is running, you can access the application at http://127.0.0.1:8000. To access the admin panel, go to http://127.0.0.1:8000/admin and log in with the superuser account.**