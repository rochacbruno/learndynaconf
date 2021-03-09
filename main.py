# -- Import the settings that you created on `config.py`
from config import settings


# -- Access the variables using dot notation
print(settings.NAME)  # outputs: Bruno

# -- You can also access using dict like notation
print(settings["NAME"])  # outputs: Bruno

# -- Access is case insensitive so you achieve the same with
print(settings.name)  # outputs: Bruno
print(settings["name"])  # outputs: Bruno

# If you are not sure that a value exists, use dict like .get Lookup
#                      KEY          DEFAULT Value if doesn't exist
print(settings.get("DoesThisExist", "looks like doesn't exist"))  # outputs: looks like doesn't exist


# You can use Dynaconf to populate an objet
class Person:
    name: str
    db: dict


p = Person()

settings.populate_obj(p, keys=["NAME", "DB"])  # only first level keys, all upper case.

print(p.NAME)        # outputs: Bruno
print(p.DB["PORT"])  # outputs: 8181


# You can use dot notation to get nested values
print(settings.db.port)                         # outputs: 8181
print(settings['db.server'])                    # outputs: Bruno.com
print(settings.get("db.password", "changeme"))  # outputs: NewSecret789


print(settings.db['timeout'])  # this was computed by the Validator, see `config.py`
                               # outputs: 11520

# Remember our lazy computed values? from `.env` file using `@jinja`.
print(settings.doubles_list)  # this is going to be computed on access, see `.env`
                              # outputs: [2 4 6 8 ]


# Feature flags? you can programatically switch environments :)
with settings.using_env('production'):
    # now values comes from [production] section of config files
    print(settings.NAME)  # outputs: Root

# not production anymore
print(settings.NAME)  # outputs: Bruno


# CONGRATS!!! You are now a Certified Dynaconf User :)

# Go to dynaconf.com and learn more on how to use it with Flask, Django
# how to extend it and contribute

# thanks :)
