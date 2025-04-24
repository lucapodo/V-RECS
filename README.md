# V-RECS

This repository contains all the supplemental materials and a demo application related to the research paper "V-RECS, a Low-Cost LLM4VIS Recommender with Explanations,
Captioning and Suggestions" (arXiv:2406.15259). It includes code, data, and resources necessary for replicating the experiments and testing the model locally. The demo application provides a hands-on way to interact with the model, allowing users to test its capabilities in generating controlled text outputs. The repository serves as a comprehensive resource for researchers and developers interested in exploring the implementation and potential applications of the proposed approach.

You can test and access the model here [HuggingFaces Model repo](https://huggingface.co/DeepvizLab/vrecs) [NOTE: you have to expose the model as TGI endpoint in HF]

## Setup


### 1. Clone the Repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/lucapodo/V-RECS.git
cd V-RECS
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

You should deploy the model on the HF 🤗 inference endpoint and copy the link to env file variable.

### 6. Run Streamlit frontend
Finally, within the V-RECS folder open a new terminal and run
```bash
streamlit run app.py
```
This will launch the frontend to test the model


## Project Structure

- `app.py`: Main application file.
- `src/`: Source code including pages, components, and utilities.
- `assets/`: Static assets like images and styles.
- `resources/`: Additional resources as supplemental paper materials and evaluation samples


