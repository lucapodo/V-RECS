# Streamlit Project Example

This project is a simple Streamlit application showcasing basic project structure and organization.

## Setup


### 1. Clone the Repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/streamlit-project.git
cd streamlit-project
```

### 2. Create a Virtual Environment
Create a virtual environment to manage your dependencies. This helps to keep the project isolated from other projects on your machine.

For **Windows**:
```bash
python -m venv venv
```

For **macOS/Linux**:
```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment
Activate the virtual environment using the following commands:

For **Windows**:
```bash
venv\Scripts\activate
```

For **macOS/Linux**:
```bash
source venv/bin/activate
```

### 4. Install Dependencies
Install the required packages using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 5. Create an `.env` File
Create an `.env` file in the project's root directory to specify the following environment variable:
```plaintext
HF_ENDPOINT=your_huggingface_endpoint_here
```


## Project Structure

- `app.py`: Main application file.
- `src/`: Source code including pages, components, and utilities.
- `assets/`: Static assets like images and styles.
- `resources/`: Additional resources as supplemental paper materials and evaluation samples


