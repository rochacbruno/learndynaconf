# -- First you import Dynaconf
from dynaconf import Dynaconf, Validator

# -- Then you create your `settings` instance
settings = Dynaconf(
    settings_files=[                  # Paths or globs to any toml|yaml|ini|json|py
        "default_settings.toml",      # a file for default settings
        "settings.toml",              # a file for main settings
        ".secrets.toml"               # a file for sensitive data (gitignored)
    ],

    environments=True,                # Enable layered environments
                                      # (sections on config file for development, production, testing)

    load_dotenv=True,                 # Load envvars from a file named `.env`
                                      # TIP: probably you don't want to load dotenv on production environments
                                      #      pass `load_dotenv={"when": {"env": {"is_in": ["development"]}}}

    envvar_prefix="DYNACONF",         # variables exported as `DYNACONF_FOO=bar` becomes `settings.FOO == "bar"`
    env_switcher="ENV_FOR_DYNACONF",  # to switch environments `export ENV_FOR_DYNACONF=production`

    dotenv_path="envfile/.env"        # custom path for .env file to be loaded
)
# More options on https://www.dynaconf.com/configuration/


# -- Lets add some Validation and Defaults
settings.validators.register(
    # Must there be a NAME defined
    # under [development] env (run mode) the name should be equal to "Bruno"
    Validator("NAME", must_exist=True, eq="Bruno", env="development"),
    # under [production] the name should be equal to "Root"
    Validator("NAME", must_exist=True, eq="Root", env="production"),
    # there must be a DB dictionary, having a PORT as integer
    Validator("DB.PORT", must_exist=True, is_type_of=int),
    # under the env [production] its value must be >=8000 and <=9000
    Validator("DB.PORT",gte=8000, lte=9000, env="production"),

    # Defaults can also be provided here (however in the [default] section of files is better)
    Validator("DB.USER", default="admin"),
    Validator("FACTOR", default=8),

    # Defaults can also be used to define computed values if default=a_callable
    Validator("DB.TIMEOUT", default=lambda _settings, _value: 24 * 60 * _settings.factor),

    # You can compound validators for better meaning
    Validator("DB.USER", ne="pgadmin") & Validator("DB.USER", ne="master"),

    # You can validate a key ONLY IF other exits
    # Password must be defined if user is defined
    Validator("DB.PASSWORD", must_exist=True, when=Validator("DB.USER", must_exist=True)),
)

# Validators are also Lazy and you need to invoke the validation
# TIP:"Experiment removing NAME from settings.toml" and then run to see the ValidationError
settings.validators.validate()

# More details on https://www.dynaconf.com/validation/

# NOTE: On Dynaconf 4.0.0 all the above will be also possible as a pydantic schema :)


# NOW go and read the `default_settings.toml` file
