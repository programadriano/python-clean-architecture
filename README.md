# Clean Architecture Example in Python - Finance Domain

This project demonstrates how to implement the Clean Architecture in a Python project focused on the finance domain. By following the Clean Architecture principles, we ensure that our application's business logic is decoupled from frameworks, UI, and databases, allowing for easier maintenance, testing, and future modifications.

## Project Structure

The project is organized into several layers, each with its own responsibility:

- `domain/`: Contains entities (domain models) and business logic. Interfaces for repositories or other external services used by use cases are also defined here.
- `application/`: Implements the use cases of the application, orchestrating the flow of data between the user interface and the domain layer.
- `adapters/`: Transforms data between the application layer and external services or interfaces, such as databases or web APIs.
- `infrastructure/`: Provides concrete implementations for the interfaces defined in the domain, like database access, file systems, and web services.

## Installation

To set up the project environment and install necessary dependencies, follow these steps:

1. **Clone the repository:**

```bash
pip install -r requirements.txt
```

This command installs FastAPI and Uvicorn, among other dependencies.

## Running the Application
Start the application:

```bash
uvicorn main:app --reload
```

This command starts the development server with hot reload enabled.

## Access the API documentation:

Open your browser and navigate to `http://127.0.0.1:8000/docs`. This page displays the interactive API documentation (Swagger UI) provided by FastAPI.

## Testing

Run unit tests by executing:

```bash
pytest
```

This ensures that the business logic and use cases behave as expected.



