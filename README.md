# bee_movie_script_tiktok
A script to send the entire bee movie script one word at a time
Used the twilio API.

Steps -

- Sign up for twilio, get your SID and AUTH_TOKEN and set the environment variables.
```
  export TWILIO_ACCOUNT_SID='{twilio_account_sid}'
  export TWILIO_AUTH_TOKEN='{twilio_auth_token}'
```
- Create a new virtual environment with the following Python 3 command - `python3 -m venv pywhatsapp`
(For python 2, first install `virtualenv` and run `virtualenv pywhatsapp`)

- Activate the virtual environment - `source ./pywhatsapp/bin/activate`
- Install the twilio helper lib (in virtualenv) - `pip install twilio`
- Connect to the Twilio sandbox
- Run your little whatsapp.py script that sends the entire script to the target number word by word!
