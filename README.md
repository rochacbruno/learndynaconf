# Learn X in Y minutes when X is Dynaconf

Dynaconf is a library aimed to be the best choice to manage configuration in Python.

It can read settings from various sources including environment variables, files, config servers, vaults etc.

It works for any kind of Python programs including Flask and Django extensions.

It is highly customizable and heavily tested.

---

## Getting Started


### Run this project from your browser

Choose one option.


- **Execute this project on Gitpod** https://gitpod.io/#https://github.com/rochacbruno/learndynaconf

- **Easily explore these files on** https://github.surf/rochacbruno/learndynaconf

- **Explore this project on repl.it** https://repl.it/@rochacbruno/dynaconfplayground#README.md

### Execute this project locally

Requirements: Python 3.6+

```bash
git clone https://github.com/rochacbruno/learndynaconf.git
cd learndynaconf
pip install dynaconf jinja2
```

Run

```py
python main.py
dynaconf -i config.settings –help
dynaconf -i config.settings list
```

---

## Explore

Open and read the files on this project in the following order

1. **`config.py`** (settings and validation)  <- **START READING THIS**
2. **default_settings.toml**  (default values)
3. **settings.toml**   (main settings)
4. **.secrets.toml**  (gitignored sensitive settings)
5. **envfile/.env**  (environment variables exported)
6. **`main.py`** (the main program)

---

Full docs on https://dynaconf.com

---

- Learn more on: https://dynaconf.com
- Contribute on: https://github.com/rochacbruno/dynaconf
- Sponsor on: https://opencollective.com/dynaconf
- Pro support on: https://xscode.com/rochacbruno/dynaconf

thanks

Bruno - https://twitter.com/rochacbruno
