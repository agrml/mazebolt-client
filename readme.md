1. Install pyenv: https://linux-notes.org/ustanovka-pyenv-v-unix-linux/
2. pyenv install 3.10.0
3. If pyenv could not build python, use bare installation: https://computingforgeeks.com/how-to-install-python-on-debian-linux/
4. pip install poetry
5. poetry build
6. poetry run uvicorn client.api:app  # port 8000 is expected in Django config
