# test.sh

# export and run the test script
export SQLALCHEMY_TRACK_MODIFICATIONS_FLAG=False && python3 -m unittest tests/test_api.py