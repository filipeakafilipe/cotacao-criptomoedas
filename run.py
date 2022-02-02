from src.infra.config.db_config import create_tables
from src.main.composer.insert_currencies import insert_currencies_composer
from src.main.composer.monitor_currencies import monitor_currencies_composer

if __name__=="__main__":
    try:
        create_tables()
        insert_currencies_composer()
        monitor_currencies_composer()
    except:
        pass
