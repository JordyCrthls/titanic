# FastAPI Project

This is a machine learning project which uses a FastAPI service to provide predictions.

## Getting Started

These instructions will get the project up and running on your local machine.

### Prerequisites

You need to have Python 3.8 and pip installed on your machine.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JordyCrthls/titanic.git
   ```

2. Navigate to the project directory:
   ```bash
   cd titanic
   ```

3. Install the Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Start the server:
   ```bash
   uvicorn main:app --reload
   ```
You can access the server at `http://localhost:8000`.

Run the Docker container on your machine:

You can now access the FastAPI server at `http://localhost:8000`.

Note: docker doesnt work, there are multiple lib version conflicts where I am not able to solve them, for example lib a and b who are dependent on x but do not support a common version of x.
