# gispro setup

git clone https://github.com/pabin/gispro

virtualenv -p python3 env

source env/bin/activate

pip install -r requirements.txt

cd gispro


python3 migrate

python manage.py runserver
