import logging
from colorama import Fore, Style, init
import openConfig


debug = openConfig.getConfig()["DEBUG"]

# Инициализация colorama (необходима для Windows)
init()

# Определяем цветные метки уровней логов
class CustomFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': Fore.CYAN,
        'INFO': Fore.GREEN,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.MAGENTA
    }

    def format(self, record):
        levelname = record.levelname
        # Добавляем цвет к меткам уровней логов
        color = self.COLORS.get(levelname, Fore.WHITE)
        record.levelname = f"{color}{levelname}{Style.RESET_ALL}"
        return super().format(record)

# Настраиваем логирование с использованием кастомного формата
handler = logging.StreamHandler()
handler.setFormatter(CustomFormatter("[%(levelname)s] %(message)s"))




def getLogger():

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG if debug else logging.INFO)
    logger.addHandler(handler)

    return logger
