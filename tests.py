# Tests for various aspects of the code

import requests

import sys

from pc_flask_server.email_utils import send_mail


def test_gallery_selection():
    test_json = {'fileName': 'non_existing_file.txt'}
    res = requests.post('http://127.0.0.1:5001/gallery/selection', json=test_json)
    print(res.status_code, res.text)
    assert res.status_code == 200
    assert res.text == "OK"


def test_send_mail():
    to = ["csci5127.grandtotem@gmail.com"]
    subject = "Test Email"
    text = "This email was generated by automated software tests for the PC flask server."
    send_mail(to, subject, text)


def run_tests():
    test_gallery_selection()

    from pc_flask_server import create_app
    with create_app().app_context():
        test_send_mail()

    sys.exit(0)


if __name__ == "__main__":
    run_tests()