## Project Setup Steps

### Clone Project Repository
```
git clone https://github.com/pabin/gispro
cd gispro
```

### Create and Activate Virtual Environment
```
virtualenv -p python3 ../env
source ../env/bin/activate
```

### Install Packages
```
pip install -r requirements.txt
```

### Database Migration with default sqlite3
```
python manage.py migrate
```

### Create Super User
```
python manage.py createsuperuser
```


### Run Project
```
python manage.py runserver
```

## Screenshots
### Object Detection
![ScreenShot](https://github.com/pabin/gispro/blob/master/object-detection.jpg?raw=true)

### Home screen
![ScreenShot](https://github.com/pabin/gispro/blob/master/assets/sreenshots/gispro_img2.png?raw=true)

### Facebook pages list
![ScreenShot](https://github.com/pabin/gispro/blob/master/assets/sreenshots/gispro_img2.png?raw=true)
