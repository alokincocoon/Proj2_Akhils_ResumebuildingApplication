import json
from typing import Any
from database import session
from litestar.config.cors import CORSConfig
from litestar import Litestar, get, post, put, delete, Request
from models import (
    ApplicantDetails,
    AddressDetails,
    Skills,
    Projects,
    Education,
    WorkExperience,
    SocialMedia,
)


def cleaned_record(record):
    """This function cleans the incoming record by eliminating
       unnecessary keys and their corresponding values.
       """
    for key in ["_sa_instance_state", "applicant_details_id", "id"]:
        record.pop(key)
    return record


def result_set(records):
    """This function returns data in the form of a list of dictionaries
       for fields where multiple entries are possible in the input page.
       Regardless of whether there is a single data entry or multiple entries,
       the final result will always be a list of dictionaries.
       """
    record_lis = []
    if records.count() == 1:
        record = records.first().__dict__
        record = cleaned_record(record)
        new_record = {}
        if record:
            for key, value in record.items():
                new_record[key] = str(value)
            record_lis.append(new_record)
        return record_lis

    elif records.count() > 1:
        for record in records.all():
            record = cleaned_record(record.__dict__)
            for key, value in record.items():
                record[key] = str(value)
            record_lis.append(record)
        return record_lis


@get("/resumes/", name="get_all_resumes")
async def display_all() -> json:
    """This function will fetch all resumes from the DB
    to display in the listing page.
    """
    records = session.query(ApplicantDetails).all()
    all_records = {}
    for record in records:
        record_id = record.id
        data = record.__dict__
        data.pop("_sa_instance_state", None)
        key = f"record_{record_id}"
        value = data
        all_records[key] = value
        json_data = json.dumps(all_records)
    return json_data


@get("/resume/{field_id: int}", name="get_resume_by_id")
async def display_by_id(field_id: int) -> json:
    """This function will fetch records according to their id."""

    all_data = {}  # dictionary to store all records

    """The data in the corresponding tables are collected here to 
    their respective variables. After that the data is returned 
    in the form of a key-value pair using the 'all_data' dictionary.
    """

    # Collecting ApplicantDetails data
    applicant_record = (
        session.query(ApplicantDetails).filter_by(id=field_id).first().__dict__
    )
    applicant_record.pop("_sa_instance_state", None)
    all_data["PersonalDetails"] = applicant_record

    # Collecting AddressDetails data
    address_record = session.query(AddressDetails).filter_by(applicant_details_id=field_id).first().__dict__
    all_data["addressDetails"] = cleaned_record(address_record)

    # Collecting Skills data
    skills_record = session.query(Skills).filter_by(applicant_details_id=field_id)
    all_data["skillList"] = result_set(skills_record)

    # Collecting Projects data
    projects_record = session.query(Projects).filter_by(applicant_details_id=field_id)
    all_data["projectDetails"] = result_set(projects_record)

    # Collecting SocialMedia data
    media_record = session.query(SocialMedia).filter_by(applicant_details_id=field_id)
    all_data["socialMediaDetails"] = result_set(media_record)

    # Collecting Education data
    education_record = session.query(Education).filter_by(applicant_details_id=field_id)
    all_data["educationDetails"] = result_set(education_record)

    # Collecting WorkExperience data
    work_record = session.query(WorkExperience).filter_by(applicant_details_id=field_id)
    all_data["workExperienceDetails"] = result_set(work_record)

    # Returning the collected data in the form of JSON
    json_data = json.dumps(all_data)
    return json_data


@get("/find-resume/{field_val: str}", name="find_resume_by_field")
async def display_by_field(field_val: str) -> json:
    """This function will fetch records according to their email id."""
    record = session.query(ApplicantDetails).filter_by(email=field_val).first()
    data = record.__dict__
    data.pop("_sa_instance_state", None)
    json_data = json.dumps(data)
    return json_data


@post("/new-resume")
async def add_data(request: Request, data: dict[str, Any]) -> json:
    """This function will save the incoming data to the DB, to their
    corresponding tables. 'applicant_details' is an object of ApplicantDetails
    model which is used to save the data to ApplicantDetails model.
    """
    commit_flag= False
    applicant_details = ApplicantDetails(
        full_name=data["PersonalDetails"].get("full_name"),
        email=data["PersonalDetails"].get("email"),
        phone_number=data["PersonalDetails"].get("phone_number"),
        image_url=data["PersonalDetails"].get("image_url"),
        summary=data["PersonalDetails"].get("summary"),
    )
    if applicant_details:
        session.add(applicant_details)
        session.commit()
        commit_flag = True
        # print(applicant_details.__dict__)
    if commit_flag:
        records = session.query(ApplicantDetails).all()
        record_lis = [ rec.__dict__ for rec in records]
        *_, applicant_record = record_lis
        # print(applicant_record)

    #  address_details object which saves data to AddressDetails model
    address_details = AddressDetails(
        applicant_details_id=applicant_record["id"],
        address_line=data["addressDetails"].get("address_line"),
        street_name=data["addressDetails"].get("street_name"),
        city=data["addressDetails"].get("city"),
        country=data["addressDetails"].get("country"),
        zip_code=data["addressDetails"].get("zip_code"),
    )
    if address_details:
        # print(address_details.__dict__)
        session.add(address_details)
        # print(address_details.__dict__)

    # Here the values are retrieved from a nested dictionary
    # The input data resides in a list belonging to the parent dictionary.
    if data["educationDetails"]:
        levels_of_education = len(data["educationDetails"])
        for entry in range(levels_of_education):
            education = Education(
                applicant_details_id=applicant_record["id"],
                qualification = data["educationDetails"][entry].get("qualification"),
                course_name = data["educationDetails"][entry].get("course_name"),
                institute_name = data["educationDetails"][entry].get("institute_name"),
                location = data["educationDetails"][entry].get("location"),
                academic_year_startdate = data["educationDetails"][entry].get(
                    "academic_year_startdate"
                ),
                academic_year_enddate = data["educationDetails"][entry].get(
                    "academic_year_enddate"
                ),
            )
            if education:
                # print(education.__dict__)
                session.add(education)

    if data["workExperienceDetails"]:
        places_worked = len(data["workExperienceDetails"])
        for entry in range(places_worked):
            work_experience = WorkExperience(
                applicant_details_id=applicant_record["id"],
                organization=data["workExperienceDetails"][entry].get("organization"),
                job_title=data["workExperienceDetails"][entry].get("job_title"),
                job_location=data["workExperienceDetails"][entry].get("job_location"),
                job_key_role=data["workExperienceDetails"][entry].get("job_key_role"),
                job_start_date=data["workExperienceDetails"][entry].get(
                    "job_start_date"
                ),
                job_end_date=data["workExperienceDetails"][entry].get("job_end_date"),
            )
            if work_experience:
                # print(work_experience.__dict__)
                session.add(work_experience)

    if data["socialMediaDetails"]:
        existing_accounts = len(data["socialMediaDetails"])
        for entry in range(existing_accounts):
                social_media = SocialMedia(
                applicant_details_id=applicant_record["id"],
                network=data["socialMediaDetails"][entry].get("network"),
                media_name=data["socialMediaDetails"][entry].get("media_name"),
                url=data["socialMediaDetails"][entry].get("url"),
            )
        if social_media:
            # print(social_media.__dict__)
            session.add(social_media)

    if data["skillList"]:
        number_of_skills = len(data["skillList"])
        for entry in range(number_of_skills):
            skills = Skills(
                applicant_details_id=applicant_record["id"],
                skill=data["skillList"][entry].get("skill"),
                skill_level=data["skillList"][entry].get("skill_level"),
            )
            if skills:
                # print(skills.__dict__)
                session.add(skills)

    if data["projectDetails"]:
        number_of_projects = len(data["projectDetails"])
        for entry in range(number_of_projects):
            projects = Projects(
                applicant_details_id=applicant_record["id"],
                project_name=data["projectDetails"][entry].get("project_name"),
                skills=data["projectDetails"][entry].get("skills"),
                project_description = data["projectDetails"][entry].get(
                    "project_description"
                ),
            )
            if projects:
                # print(projects.__dict__)
                session.add(projects)

    # The received data is commited to the database
    session.commit()
    return data


@put("/edit-data/{applicant_id: int}")
async def edit_data(applicant_id: int, data: dict[str, Any]) -> json:
    applicant_detail_record = (
        session.query(ApplicantDetails).filter_by(id=applicant_id).first()
    )
    if applicant_detail_record:
        applicant_detail_record.full_name = data["PersonalDetails"]["full_name"]
        applicant_detail_record.email = data["PersonalDetails"]["email"]
        applicant_detail_record.phone_number = data["PersonalDetails"]["phone_number"]
        applicant_detail_record.image_url = data["PersonalDetails"]["image_url"]
        applicant_detail_record.summary = data["PersonalDetails"]["summary"]
        session.add(applicant_detail_record)

    address_detail_record = (
        session.query(AddressDetails).filter_by(id=applicant_id).first()
    )
    if address_detail_record:
        address_detail_record.address_line = data["addressDetails"]["address_line"]
        address_detail_record.street_name = data["addressDetails"]["street_name"]
        address_detail_record.city = data["addressDetails"]["city"]
        address_detail_record.country = data["addressDetails"]["country"]
        address_detail_record.zip_code = data["addressDetails"]["zip_code"]
        session.add(address_detail_record)

    education_detail_record = (
        session.query(Education).filter_by(id=applicant_id).all()
    )
    if education_detail_record:
     item=0
     for entry in education_detail_record:
        education_data = data.get("educationDetails")[item]
        education_detail_record.qualification = education_data.get("qualification")
        education_detail_record.course_name = education_data.get("course_name")
        education_detail_record.institute_name = education_data.get["institute_name"]
        education_detail_record.location = education_data.get["location"]
        education_detail_record.academic_year_startdate = education_data.get["academic_year_startdate"]
        education_detail_record.academic_year_enddate = education_data.get["academic_year_enddate"]
        session.add(entry)
        item +=1

    work_detail_record = (
        session.query(WorkExperience).filter_by(id=applicant_id).all()
    )
    if work_detail_record:
        item = 0
        for entry in work_detail_record:
          workeducation = data.get("workExperienceDetails")[item]
          work_detail_record.organization = workeducation.get("organization")
          work_detail_record.job_title = workeducation.get("job_title")
          work_detail_record.job_location = workeducation.get("job_location")
          work_detail_record.job_key_role = workeducation.get("job_key_role")
          work_detail_record.job_start_date = workeducation.get("job_start_date")
          work_detail_record.job_end_date = workeducation.get("job_end_date")
          session.add(entry)
          item +=1

    skill_detail_record = (
        session.query(Skills).filter_by(id=applicant_id).all()
    )

    if skill_detail_record:
        item = 0
        for entry in skill_detail_record:
            skill_data = data.get("skillList")[item]
            skill_detail_record.skill = skill_data.get("skill")
            skill_detail_record.skill_level = skill_data.get("skill_level")
            session.add(entry)
            item +=1

    project_detail_record = (
        session.query(Projects).filter_by(id=applicant_id).all()
    )
    if project_detail_record:
        item = 0 
        for entry in project_detail_record:
         project_data = data.get("projectDetails")[item]
         project_detail_record.project_name =  project_data.get("project_name")
         project_detail_record.skills = project_data.get("skills")
         project_detail_record.project_description = project_data.get("project_description")
         session.add(entry)
         item +=1

    socialmedia_detail_record = ( 
        session.query(SocialMedia).filter_by(id=applicant_id).first()
    )

    if socialmedia_detail_record:
        item = 0
        for entry in socialmedia_detail_record:
            social_data = data.get("socialMediaDetails")[item]
            socialmedia_detail_record.network = social_data.get("network")
            socialmedia_detail_record.media_name = social_data.get("media_name")
            socialmedia_detail_record.url = social_data.get("url")
        session.add(socialmedia_detail_record)

    session.commit()
    return json.dumps(data)

@delete("/delete-resume/{applicant_id: int}")
async def delete_data(applicant_id: int) -> None:
    query = session.query(ApplicantDetails).filter_by(id=applicant_id).first()
    if query:
        session.delete(query)
        session.commit()
        return None
    
cors_config = CORSConfig(
    allow_origins=["*"]
 )


app = Litestar(
    [
        display_all,
        display_by_id,
        display_by_field,
        add_data,
        edit_data,
        delete_data,
    ],
cors_config=cors_config,
debug=True
    
)
