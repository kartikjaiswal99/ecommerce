# E-commerce API

This project is an E-commerce API built using Django and Django REST Framework. It includes functionalities for managing products, handling user authentication, integrating payment processing, and more. Docker is used for creating isolated development environments, and automated testing is conducted using Pytest to ensure reliability.

## Features

- **RESTful API Development**: Built using Django and Django REST Framework.
- **Admin Site for Sellers**: Manage product listings, including adding, updating, and deleting products.
- **Cart Functionality**: Add items to the cart without logging in, enhancing user convenience.
- **Secure Authentication**: Implemented using JWT (JSON Web Tokens).
- **Payment Processing**: Integrated with Flutterwave for secure and efficient payment handling.
- **Optimized Performance**: Database queries optimized using Django ORM for enhanced performance and reduced response times.
- **Isolated Development Environments**: Utilized Docker to ensure consistency across different setups.
- **Automated Testing**: Conducted using Pytest to ensure reliability and performance.

## Technologies Used

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Django REST Framework**: A powerful and flexible toolkit for building Web APIs.
- **Docker**: A platform for developing, shipping, and running applications inside containers.
- **JWT**: JSON Web Tokens for secure user authentication.
- **Flutterwave**: A payment processing service for integrating payment gateways.
- **Pytest**: A framework that makes building simple and scalable test cases easy.

### Usage
1. **Clone the Repository**
   ```bash
   git clone https://github.com/kartikjaiswal99/ecommerce.git
   ```

2. **Pull the Docker Image**
   ```bash
   docker pull kartik5180/e-commerce_api
   ```

3. **Run the Docker Container**
   If you pulled the image directly from Docker Hub, you might use:
   ```bash
   docker run -p 8000:8000 kartik5180/e-commerce_api:latest
   ```

4. **Accessing the API**
   Once the container is running, you can access the API from your web browser or tools like Postman:
   ```bash
   http://localhost:8000/
   ```
#### Notes
- Ensure Docker is installed and running on your machine before running the commands.
