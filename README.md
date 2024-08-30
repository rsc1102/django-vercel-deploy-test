# django-vercel-deploy-test
Repository to test how to deploy django apps to Vercel

## Steps
1. &lt;project-name>/settings.py
```python 
ALLOWED_HOSTS = ['.vercel.app']

MIDDLEWARE = [
    ...
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ...
]

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```
1. &lt;project-name>/wsgi.py:
```python 
app = application
```
1. vercel.json
```json
{
    "builds": [
      {
        "src": "<project-name>/wsgi.py",
        "use": "@vercel/python",
        "config": { "maxLambdaSize": "15mb", "runtime": "python3.12" }
      },
      {
        "src": "build_files.sh",
        "use": "@vercel/static-build",
        "config": {
          "distDir": "staticfiles"
        }
      }
    ],
    "routes": [
      {
        "src": "/(.*)",
        "dest": "<project-name>/wsgi.py"
      }
    ],
    "outputDirectory": "staticfiles"
  }
```
1. build_files.sh
```bash
#!/usr/bin/env bash

echo "Creating virtual env"
python3.12 -m venv myenv
source myenv/bin/activate

echo "Upgrading pip"
python3.12 -m pip install --upgrade pip

echo "Installing dependencies"
python3.12 -m pip install -r requirements.txt

echo "Collecting static files"
python3.12 manage.py collectstatic --no-input --clear

echo "build_files.sh process complete. Folder list:"
ls
```