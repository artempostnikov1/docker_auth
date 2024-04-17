from flask import Flask, request, abort
import os


app = Flask(__name__)

root_passwd_storage = {}  # map container name to it's root password


def is_user_allowed_from_id(user: str) -> bool:
    '''
    mock method: is user allowed to connect to container as root
    '''
    return True


def gen_root_passwd():
    ...


def set_container_root_passwdw():
    os.system(...)


def make_python_cron():
    ...


@app.route("/")
def hello_world():

    auth_str = str(request.authorization).lower().strip()
    cur_user = request.args.get('user')

    if auth_str != 'some-rnd-string':
        abort(403)


if __name__ == '__main__':
    app.run()