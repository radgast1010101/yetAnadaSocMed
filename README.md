# README 
## yetAnadaSocMed ai project

1. Pull Code to PythonAnywhere
Open a Bash Console on PythonAnywhere (at root e.g. /home/your-site-name/) and clone your repo:

(at Bash)
```
cd ~
, git clone https://github.com/radagast1010101/yetAnadaSocMed.git
cd yetAnadaSocMed
```

2. Setup the Environment (if, not yet started/set)
Create a virtual environment so your Gemini libraries don't break:

(at Bash)
Create the environment
```
mkvirtualenv my-env --python=/usr/bin/python3.10
```

Install the libraries (at  /home/your-site-name/yetAnadaSocMed/ where manage.py file is)

(at Bash)
```
pip install -r requirements.txt
```

4. Configure the Web Tab
Go to the Web tab on the PythonAnywhere dashboard and set these paths:

Source Code: /home/your-site-name/yetAnadaSocMed
Working Directory: /home/your-site-name/yetAnadaSocMed
Virtualenv: my-env (Just type the name you gave it)

5. Set Your API Keys (The Secret Step)
Since we ignored the .env file, you need to tell PythonAnywhere your Gemini Key.

add your keys at /home/your-site-name/yetAnadaSocMed/yetAnadaSocMed/settings.py below

SECURITY WARNING: keep the secret key used in production secret!
- SECRET_KEY = "<YOUR_SECRET_KEY_HERE>" <-- add pythonanywhere secret key

AI, might cause 500 error if none
- GEMINI_API_KEY="<YOUR_GEMINI_API_KEY>" <-- register and add gemini api key at google ai studio

6. Database & Static Files
Back in the Bash Console, run your migrations:

(at Bash)
python manage.py migrate
python manage.py collectstatic

---

for more info...

See https://help.pythonanywhere.com/ (or click the "Help" link at the top
right) for help on how to use PythonAnywhere, including tips on copying and
pasting from consoles, and writing your own web applications.

