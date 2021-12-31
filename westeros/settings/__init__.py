import os

from .base import *
from .configuration import *


# load environment, by default set to local
env = os.environ.get("ENVIRONMENT", "LOCAL")

if env == "PROD":
    from .prod import *
elif env == "LOCAL":
    from .local import *
elif env == "CI":
    from .ci import *

