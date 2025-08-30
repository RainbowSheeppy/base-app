# Base App

A minimal FastAPI application skeleton with SQLModel and PostgreSQL integration.  
Designed as a flexible foundation for building modern backend services.

## Features

- FastAPI for building APIs
- SQLModel for ORM and data modeling
- PostgreSQL integration
- Ready for Docker containerization
- Code formatting and linting with Ruff

## Getting Started

1. Install dependencies:
    ```sh
    uv sync --frozen
    ```

## How to Run with Docker Compose

1. Build and start the application:
    ```sh
    docker-compose up --build
    ```

The API will be available at [http://localhost:8000](http://localhost:8000).

## License

MIT