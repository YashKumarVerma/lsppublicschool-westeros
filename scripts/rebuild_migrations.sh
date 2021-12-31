find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

psql -U postgres < "DROP DATABASE lsp_westeros;"

python manage.py makemigrations
python manage.py migrate