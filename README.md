# Learn X in Y minutes when X is Dynaconf

Dynaconf is a library aimed to be the best choice to manage configuration in Python.

It can read settings from various sources including environment variables, files, config servers, vaults etc.

It works for any kind of Python programs including Flask and Django extensions.

It is highly customizable and heavily tested.

> **TIP:** You can click `run` button above to run this example and see the output on the terminal on the sidebar.
> For more real examples, open and explore the files on this project in the following order
> - **config.py** (settings and validation) 
> - **default_settings.toml**  (default values) 
> - **settings.toml**   (main settings)  
> - **.secrets.toml**  (gitignored sensitive settings) 
> - **.env**  (environment variables exported) 
> - **main.py** (the main program)

> **another tip**: Open the `shell` on the sidebar and run 
> ```py
> dynaconf -i config.settings list
> ```

---

## Getting started

Full docs on https://dynaconf.com

### install

The first thing you need is to install Dynaconf 

```bash
pip install dynaconf
```

---

### Create your settings instance

Then you need to create your settings instance and provide the configuration you need to customize dynaconf 
You can also stick with the defaults.

`yourproject/config.py`
```py
from dynaconf import Dynaconf 

settings = Dynaconf(
    settings_files=["settings.toml", "other.yaml"],
    **options
)
```

 available options on https://www.dynaconf.com/configuration/

> **TIP** there is also a `dynaconf` CLI tool to automate that coding for you. more on: https://www.dynaconf.com/cli/#dynaconf-init
 
---

### Define your settings sources 

`settings.toml`
```toml
key = "value"
```

`other.yaml`
```yaml
key: value
```

`.env`
```bash
DYNACONF_KEY=value
```

`console`

```bash
export DYNACONF_KEY=value
```

> **TIP:** Dynaconf supports `json, yaml, toml, py, ini, .env` out of the box and can also load from vault server, redis and custom sources.

---

### Access your settings instance whenever you need 

`main.py`
```py

from config import settings  # remember you instantiated on myproject/config.py

print(settings.key)

```

> **TIP**: For more real examples, open and explore the files on this project in the following order
> - **config.py** (settings and validation)
> - **default_settings.toml**  (default values)
> - **settings.toml**   (main settings)
> - **.secrets.toml**  (gitignored sensitive settings)
> - **.env**  (environment variables exported)
> - **main.py** (the main program)

---

Learn more on: https://dynaconf.com
Contribute on: https://github.com/rochacbruno/dynaconf
Sponsor on: https://opencollective.com/dynaconf
Pro support on: https://xscode.com/rochacbruno/dynaconf

thanks

Bruno - https://twitter.com/rochacbruno