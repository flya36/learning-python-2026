import logging
from pathlib import Path
log_dir = Path(__file__).resolve().parent.parent.parent / 'logs'
log_dir.mkdir(exist_ok=True)
logging.basicConfig(
    level = logging.INFO,
    format='%(asctime)s | %(name)-8s | %(levelname)s | %(message)s',
    handlers=[
        logging.FileHandler('logs_dir/app.log',encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)