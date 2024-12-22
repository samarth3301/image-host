# Flask Image Server

This is a simple Flask application that provides an image upload and retrieval service. It allows users to upload images and retrieve them through a unique URL.

## Features

- Upload images securely using a secret key.
- Retrieve uploaded images through a URL.
- Customizable upload directory and domain URL.
- Randomly generated filenames for uploaded images to avoid conflicts.

## Prerequisites

- Python 3.6+
- Flask
- python-dotenv (for managing environment variables)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/samarth3301/image-host
    cd image-host
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the project directory and add the following:

    ```env
    SECRET_KEY=
    DIR=
    DOMAIN_URL=
    STRING_LEN=
    ```

5. **Run the application:**

    ```bash
    python app.py
    ```

    By default, the application will run on `http://127.0.0.1:5000`.

## Usage

### Upload an Image

To upload an image, send a POST request to `/upload` with the following form data:

- `secret`: The secret key defined in the `.env` file.
- `sharex`: The image file to be uploaded.

Example using `curl`:

```bash
curl -X POST -F "secret=" -F "sharex=@path/to/your/image.png" http://127.0.0.1:5000/upload
```
