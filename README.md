# Installation

Run the following from within the root of the repo:

```
$ python3 -m venv .
$ source bin/activate
$ pip install -r requirements.txt
```

Substitute `bin/activate` for `Scripts/activate` or `Scripts/Activate.ps1` etc as your environment requires.

You'll also need to create a Personal Access Token in JIRA see https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html for details.

Now create credentials.yml from the credentials.example.yml file and then you can run the script

```
python main.py
```
