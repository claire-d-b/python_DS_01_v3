source ~/.zshrc
python -m venv venv
source venv/bin/activate
pip install --upgrade pip

source venv/bin/activate

pip install matplotlib numpy pillow

pip install flake8
alias norminette=flake8

echo alias python='./venv/bin/python' >> venv/bin/activate
source venv/bin/activate

python rotate.py

deactivate

rm -rf **pycache**
rm -rf venv

AssertionError: Error: 'int' object is not iterable (parameter in apply_limit() is not a list)
AssertionError: Error: list index out of range (give_bmi(): length of the lists differ)
