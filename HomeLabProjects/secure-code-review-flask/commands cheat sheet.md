# Clone the repo
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo/secure-code-review-flask

# Navigate into the app folder
cd insecure-app  # or secure-app

# (Optional) Create a virtual environment
python -m venv venv

# Activate the virtual environment
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate

# Install Flask
pip install Flask

# Run the app
python app.py
