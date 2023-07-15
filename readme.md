<img src="https://raw.githubusercontent.com/kkamara/useful/915937134e2f0b541e50594a9e3c630df56d8c29/see-message-java-mobile.png" alt="see-message-java-mobile.png" />

# Python Web



## Requirements

* [Python](https://www.python.org).

## Installation

```bash
pip3 install virtualenv
virtualenv .venv
source .venv/bin/activate
(.venv) pip3 install -r requirements.txt
```

## Usage

```bash
(.venv) # alias py3="python3"
(.venv) py3 manage.py runserver 8000
```

## iPython Django Shell

```bash
(.venv) python3 manage.py shell -i ipython
```

## API

```bash
(.venv) python manage.py show_urls
```

View the api collection [here](https://documenter.getpostman.com/view/17125932/UVyxQYrt).

## Admin

```bash
(.venv) export DJANGO_SUPERUSER_PASSWORD=secret

(.venv) python manage.py createsuperuser \
  --username admin_user \
  --email admin@foobarbazz.com \
  --no-input
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[BSD](https://opensource.org/licenses/BSD-3-Clause)
