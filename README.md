# Flask Project Name
FlaskProject

# Description
This repository contains an assignment for the “Introduction to Web Application Technology” course.

# Technologies Used
- Python 3.x
- Flask
- HTML / CSS (optional)
- SQLite 

# Project Structure
```
FlaskProject/
│
├── static/
│   ├── script.js
│   └── style.css
│   
├── templates/   
│   ├── add.html
│   └── home.html
│
├── .gitignore
├── README.md
├── app.py
├── movies.db
└── requirements.txt
```
## Files ignored by Git
The project uses `.gitignore` to exclude virtual environments, environment
variables, cache files, etc.

## Installation
1. Clone the repository:
```
git clone https://github.com/agorkaissi/FlaskProject.git
cd FlaskProject
```
2. Create a virtual environment (recommended):
```
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```
3. Install dependencies:
```
pip install -r requirements.txt
```
## Running the Application
```
flask run
```
or
```
python app.py
```
then open your browser (Tested on Brave) and open:

```
http://127.0.0.1:5000/
```
