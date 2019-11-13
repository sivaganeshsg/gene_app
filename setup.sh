# setup.sh

python3 -m venv venv
. venv/bin/activate

# install all the required packages
pip3 install -r requirements.txt

./start.sh