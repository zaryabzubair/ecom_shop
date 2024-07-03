echo "virtual environment setup"
python3.9 -m venv venv

echo "activate virtual environment"
source venv/bin/activate

echo "installing dependencies"
pip install -r requirements.txt

echo "static files"
python manage.py collectstatic --noinput