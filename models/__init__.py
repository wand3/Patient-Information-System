from models.base_model import BaseModel
from models.history import History
from models.patient import Patient

import config
CNC = config.Config.CNC
storage = config.TestConfig()
storage.reload()
