from sqlalchemy import MetaData
from sqlalchemy.ext.automap import automap_base

import src.db

m = MetaData(schema="public")
Base = automap_base(metadata=m)
Base.prepare(autoload_with=src.db.engine)

# Now you can create table classe from table names, eg.:
# TableName = Base.classes.table_name
