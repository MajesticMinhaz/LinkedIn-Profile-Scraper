from dotenv import dotenv_values
from datetime import datetime
from sqlalchemy import create_engine, BinaryExpression
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError, NoResultFound


# Get the config values from .env file
config = dotenv_values('.env')


# Define the SQLAlchemy models
Base = declarative_base()


class LinkedInData(Base):
    """Represents information about LinkedIn Data."""

    __tablename__ = "linkedin_data"

    id = Column(Integer, primary_key=True, autoincrement=True)
    profile_url = Column("profile_url", String, unique=True, nullable=False)
    first_name = Column("first_name", String, nullable=True, default=None)
    last_name = Column("last_name", String, nullable=True, default=None)
    company_name = Column("company_name", String, nullable=True, default=None)
    job_title = Column("job_title", String, nullable=True, default=None)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __init__(self, profile_url: str, **kwargs: str):
        self.profile_url = profile_url
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.company_name = kwargs.get('company_name')
        self.job_title = kwargs.get('job_title')

    def __repr__(self):
        return f'LinkedIn(profile_url={self.profile_url}, company={self.company_name})'


# create the engine and bind it to the database
engine = create_engine(url=config.get("DATABASE_URL"), echo=False)

# Create the database tables (if they don't exist)
with engine.begin() as conn:
    Base.metadata.create_all(conn)

# Create a session to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_linkedin_data(session_local: sessionmaker[Session] = SessionLocal, **kwargs: str):
    # Create the session instance
    session = session_local()

    # Create the linkedin_data instance
    linkedin_data = LinkedInData(
        profile_url=kwargs.get('profile_url'),
        first_name=kwargs.get('first_name'),
        last_name=kwargs.get('last_name'),
        company_name=kwargs.get('company_name'),
        job_title=kwargs.get('job_title')
    )

    try:
        # Add the data to the session
        session.add(instance=linkedin_data)
        # Commit the transaction
        session.commit()
        print("Data inserted successfully.")
    except IntegrityError:
        # Rollback the transaction in case of IntegrityError
        session.rollback()
        print("Data already exists. Insertion aborted.")
    finally:
        # Close the session
        session.close()


def get_linkedin_data_list(
        start_id: int, 
        end_id: int,
        logic: BinaryExpression[bool],
        selected_columns: list = [LinkedInData.id, LinkedInData.profile_url],
        session_local: sessionmaker[Session] = SessionLocal
    ):

    # session local
    session = session_local()

    # Build the query
    query = session.query(*selected_columns).filter(
        LinkedInData.id >= start_id,
        LinkedInData.id <= end_id,
        logic
    )

    # Execute the query and retrieve the results as a list of tuples
    linkedin_data_list = query.all()

    # Close the session
    session.close()

    return linkedin_data_list


def get_linkedin_data(
        logic: BinaryExpression[bool],
        session_local: sessionmaker[Session] = SessionLocal
    ):

    # session local
    session = session_local()

    # Build the query
    query = session.query(LinkedInData).filter(logic)

    # Execute the query and retrieve the result
    linkedin_data = query.first()

    # Close the session
    session.close()

    return linkedin_data


def update_linkedin_data(session_local: sessionmaker[Session] = SessionLocal, **kwargs: str):

    # Create the session instance
    session = session_local()

    try:
        # Query the database to find the LinkedInData record based on the profile_url
        linkedin_data = session.query(LinkedInData).filter_by(profile_url=kwargs.get('profile_url')).one()

        # Define a list of attributes to update
        attributes_to_update = ['first_name', 'last_name', 'company_name', 'job_title']

        # Iterate over the attributes and update them if present in kwargs
        for attribute in attributes_to_update:
            if attribute in kwargs:
                setattr(linkedin_data, attribute, kwargs[attribute])

        # Commit the transaction
        session.commit()
        # print("Data updated successfully.")
    except NoResultFound:
        print(f"Profile URL '{kwargs.get('profile_url')}' not found in the database. Update aborted.")
    finally:
        # Close the session
        session.close()


def get_linkedin_data_table(session_local: sessionmaker[Session] = SessionLocal) -> list:
    
    # Create the session instance
    session = session_local()

    try:
        # Query the database to retrieve all LinkedInData records
        linkedin_data_records = session.query(LinkedInData).all()

        # Create a list to store the retrieved data
        data_list = []

        # Iterate through the records and construct dictionaries excluding the 'id' column
        for record in linkedin_data_records:
            data = {
                "profile_url": record.profile_url,
                "first_name": record.first_name,
                "last_name": record.last_name,
                "company_name": record.company_name,
                "job_title": record.job_title
            }
            data_list.append(data)

        return dict(data=data_list)
    finally:
        # Close the session
        session.close()
