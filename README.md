# ChuckCI

Requirements:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Dev:
python main.py

Prod:
gunicorn -w 4 -b 0.0.0.0 'main:app'