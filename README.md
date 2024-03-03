# Mini Twitter

Mini Twitter is a simple Python web application built with FastAPI framework. It allows users to post short messages, similar to tweeting.

## Installation

Before running the application, make sure you have Python installed on your system. Then, follow these steps:

1. Clone the repository:

```
git clone <repository_url>
```

2. Install the project dependencies:

```
pip install -r requirements.txt
```

## Configuration

Ensure you have MongoDB installed and running on your system. Update the `config/db.py` file with your MongoDB URI.

```python
# config/db.py
from pymongo import MongoClient
import certifi

MONGO_URI = "mongodb+srv://your_username:your_password@cluster_url"

conn = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
```

## Usage

To start the application, run the following command:

```
uvicorn index:app --reload
```

This command will start the uvicorn server with auto-reload enabled. The server will be accessible at `http://localhost:8000`.

## Endpoints

- `/`: This is the root endpoint of the application where users can post tweets and view existing tweets.

## Directory Structure

- `config/db.py`: Configuration file for MongoDB connection.
- `models/note.py`: Defines the data model for tweets.
- `routes/note.py`: Defines the routes and logic for handling tweets.
- `schemas/note.py`: Defines Pydantic schemas for tweet data.
- `templates/index.html`: HTML template for the user interface.
- `index.py`: Main FastAPI application file.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs, feature requests, or suggestions.

## License

This project is licensed under the [MIT License](LICENSE).
