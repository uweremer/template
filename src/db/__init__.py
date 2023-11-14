import logging

from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker

import src


def get_db_engine(config):
    logging.basicConfig()
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    url_object = URL.create(
        "postgresql+psycopg2",
        username=config.get("DB", "POSTGRES_USER"),
        password=config.get("DB", "POSTGRES_PASSWORD"),
        host=config.get("DB", "POSTGRES_HOST"),
        port=config.get("DB", "POSTGRES_PORT"),
        database=config.get("DB", "POSTGRES_DB"),
    )
    engine = create_engine(url_object)
    return engine


def get_db_session(engine):
    Session = sessionmaker(bind=engine)
    return Session


engine = get_db_engine(src.config)
Session = get_db_session(engine)
