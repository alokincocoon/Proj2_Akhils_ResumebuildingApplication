from database import engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Date, Integer, ForeignKey

# Base class derived from a mapper
Base = declarative_base()

# Base class for creating the Applicantdetails

class ApplicantDetails(Base):
    __tablename__ = "applicant_details"

    id = Column(Integer, primary_key=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(250), nullable=False)
    phone_number = Column(String(13), nullable=False)
    image_url = Column(String(250), nullable=True)
    summary = Column(String(1000), nullable=False)


class AddressDetails(Base):
    __tablename__ = "address_details"

    id = Column(Integer, primary_key=True)
    applicant_details_id = Column(
        Integer, ForeignKey("applicant_details.id", ondelete="CASCADE")
    )
    address_line = Column(String(300), nullable=False)
    street_name = Column(String(300), nullable=False)
    city = Column(String(200), nullable=False)
    zip_code = Column(String(10), nullable=False)
    country = Column(String(200), nullable=False)
   

    # Defining the relationship with parent table
    applicant = relationship("ApplicantDetails", backref=backref("address_details", passive_deletes=True))


class Education(Base):
    __tablename__ = "education"

    id = Column(Integer, primary_key=True)
    applicant_details_id = Column(
        Integer, ForeignKey("applicant_details.id", ondelete="CASCADE")
    )
    qualification = Column(String(30), nullable=False)
    course_name = Column(String(50), nullable=False)
    institute_name = Column(String(250), nullable=False)
    location = Column(String(200), nullable=False)
    academic_year_startdate = Column(Date, nullable=False)
    academic_year_enddate = Column(Date, nullable=False)

    # Defining the relationship with parent table
    applicant = relationship("ApplicantDetails", backref=backref("education", passive_deletes=True))



class WorkExperience(Base):
    __tablename__ = "work_experience"

    id = Column(Integer, primary_key=True)
    applicant_details_id = Column(
        Integer, ForeignKey("applicant_details.id", ondelete="CASCADE")
    )
    organization = Column(String(250), nullable=True)
    job_title = Column(String(150), nullable=True)
    job_location = Column(String(200), nullable=True)
    job_key_role = Column(String(300), nullable=True)
    job_start_date = Column(Date, nullable=True)
    job_end_date = Column(Date, nullable=True)

    # Defining the relationship with parent table
    applicant = relationship("ApplicantDetails", backref=backref("work_experience", passive_deletes=True))



class SocialMedia(Base):
    __tablename__ = "social_media"

    id = Column(Integer, primary_key=True)
    applicant_details_id = Column(
        Integer, ForeignKey("applicant_details.id", ondelete="CASCADE")
    )
    network = Column(String(30), nullable=True)
    media_name = Column(String(100), nullable=True)
    url = Column(String(250), nullable=True)

    # Defining the relationship with parent table
    applicant = relationship("ApplicantDetails", backref=backref("social_media", passive_deletes=True))



class Skills(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True)
    applicant_details_id = Column(
        Integer, ForeignKey("applicant_details.id", ondelete="CASCADE")
    )
    skill = Column(String(50), nullable=True)
    skill_level = Column(String(20), nullable=True)

    # Defining the relationship with parent table
    applicant = relationship("ApplicantDetails", backref=backref("skills", passive_deletes=True))



class Projects(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    applicant_details_id = Column(
        Integer, ForeignKey("applicant_details.id", ondelete="CASCADE")
    )
    project_name = Column(String(60), nullable=True)
    skills = Column(String(100), nullable=True)
    project_description = Column(String(300), nullable=True)

    # Defining the relationship with parent table
    applicant = relationship("ApplicantDetails", backref=backref("projects", passive_deletes=True))


# Create tables in the database
Base.metadata.create_all(bind=engine, checkfirst=True)
