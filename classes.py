import enum
import telepot
from consts import *

class State(enum.Enum):
    start = 'start'
    main_menu = 'main_menu'
    kargruh = 'kargruh'
    campaign = 'campaign'
    nashrie = 'nashrie'
    admin = 'admin'
    get_nashrie = 'get_nashrie'
    get_nam = 'get_nam'
    get_codemeli = 'get_codemeli'
    get_number = 'get_number'
    get_grad = 'get_grad'
    get_mizan = 'get_mizan'
    get_ever = 'get_ever'
    get_tiz = 'get_tiz'
    get_matn = 'get_matn'
    tashakor = 'tashakor'
    get_reason = 'get_reason'


