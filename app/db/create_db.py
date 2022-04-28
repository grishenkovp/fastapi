from app.db.database import engine
from app.db.tables import Base

Base.metadata.create_all(engine)
