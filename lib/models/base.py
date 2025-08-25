from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# Database configuration
engine = create_engine('sqlite:///contributions.db')
Base = declarative_base()
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

# Create session instance
session = Session()

def create_tables():
    """Create all database tables defined in the models."""
    from .organization import Organization
    from .contributor import Contributor
    from .contribution import Contribution
    Base.metadata.create_all(engine)

def get_session():
    """Get a new database session."""
    return Session()

# Import models for create_tables to discover them
from .organization import Organization
from .contributor import Contributor
from .contribution import Contribution

__all__ = ['Base', 'engine', 'session', 'create_tables', 'get_session', 
           'Organization', 'Contributor', 'Contribution']