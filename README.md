# Simple Ecommerce Web Application [shop cart]

A simple ecommerce web application for buying and selling products.

## Table of Contents

- [Project Overview](#project-overview)
- [Setup Instructions](#setup-instructions)
  - [Backend Setup](#backend-setup)
  - [Database Setup](#database-setup)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project is a simple ecommerce web application designed to facilitate the buying and selling of products online. It provides basic features such as browsing products, adding them to a shopping cart, and making purchases.

## Setup Instructions

Follow these steps to set up the backend and database for the application.

### Backend Setup

1. Clone the repository.
2. Navigate to the `backend` directory.
3. Install dependencies: `pip install -r requirements.txt`.
4. Configure the backend settings by modifying the `configFile.py` file.
5. Run the backend server: `python app.py`.

### Database Setup

1. Install MySQL if not already installed.
2. Create a new database in MySQL.
3. Import the database dump file provided (eg.`database_dump.sql`) or execute the SQL queries in your database management tool.

## Configuration

To configure the backend settings, modify the `data.properties` file and `configFile.py` according to your requirements.

## Usage

Once the backend and database are set up, you can access the ecommerce web application through your browser. Browse products, add them to your cart, and proceed to checkout to make purchases.

## License

This project is licensed under the [MIT License](LICENSE).
