<script>
  import PersonalDetails from "./PersonalDetails.svelte";
  import AddressDetails from "./AddressDetails.svelte";
  import EducationDetails from "./EducationDetails.svelte";
  import WorkExperienceDetails from "./WorkExperienceDetails.svelte";
  import SkillsDetails from "./SkillsDetails.svelte";
  import SocialMediaDetails from "./SocialMediaDetails.svelte";
  import ProjectDetails from "./ProjectDetails.svelte";
  import ButtonInput from "../InputFields/Button.svelte";
  import Icon from "@iconify/svelte";
  import arrowLeftIcon from "@iconify/icons-mdi/arrow-left";
  import { prevent_default } from "svelte/internal";
  import {
    validateEmail,
    validatePhone,
    validateImageUrl,
    validateFullName,
    validateSummary,
    validateAddress,
    validateCity,
    validateCountry,
    validateQualification,
    validateCourseName,
    validateInstitute,
    validateInstituteLocation,
    validateZipcode
  } from "../validation";
  let showMessage = "";
  let successMessage = "";
  let warningMessage = "";
  let showError=false;
  export let formValue = {};
  // basic details
  export let full_name = "";
  export let email = "";
  export let phone_number = "";
  export let image_url = "";
  export let summary = "";

  // address details
  export let address_line = "";
  export let street_name = "";
  export let city = "";
  export let zip_code = "";
  export let country = "";

  // education details
  export let educationDetails = [
    {
      qualification: "",
      course_name: "",
      institute_name: "",
      location: "",
      academic_year_startdate: "",
      academic_year_enddate: "",
    },
  ];

  // work experience
  export let workExperienceDetails = [
    {
      job_title: "",
      organization: "",
      job_location: "",
      job_key_role: "",
      job_start_date: "",
      job_end_date: "",
    },
  ];

  // skill details
  export let skillList = [{ skill: "", skill_level: "" }];

  // socialmedia details
  export let socialMediaDetails = [{ network: "", media_name: "", url: "" }];

  // project details
  export let projectDetails = [
    { project_name: "", project_description: "", skills: "" },
  ];




  async function submitForm(){
    formValue = 
    {
      "PersonalDetails":{full_name,email,phone_number,image_url,summary},
      "addressDetails":{address_line,street_name,city,country,zip_code},
      educationDetails,
      socialMediaDetails,
      workExperienceDetails,
      skillList,
      projectDetails
    };
    let fullNameCheck = validateFullName(full_name);
    //Validate phone number
    let phoneCheck = validatePhone(phone_number);
    // Validate email
    let emailCheck = validateEmail(email);
    // Validate image url
    let imageUrlCheck = validateImageUrl(image_url);
    // Validate summary
    let summaryCheck = validateSummary(summary);
    // Validate address
    let addressCheck = validateAddress(address_line);
    // Validate phone city
    let cityCheck = validateCity(city);
    // validate state
    // validate country
    let countryCheck = validateCountry(country);
    // validate zipcode
    let zipcodeCheck = validateZipcode(zip_code)
    // Initialize an empty array to store education errors
    let educationErrors = [];
    // iterating more than one educational details
    for (let i = 0; i < educationDetails.length; i++) {
      let qualificationCheck = validateQualification(educationDetails[i].qualification);
      let coursenameCheck = validateCourseName(educationDetails[i].course_name);
      let instituteCheck = validateInstitute(educationDetails[i].institute_name);
      let instituteLocationCheck = validateInstituteLocation(
        educationDetails[i].location
      );
      if (
        qualificationCheck !== "" ||
        coursenameCheck != "" ||
        instituteCheck !== "" ||
        instituteLocationCheck !== "" 
      ) {
        educationErrors.push({
          index: i,
          qualificationError: qualificationCheck,
          courseNameError: coursenameCheck,
          instituteError: instituteCheck,
          instituteLocationError: instituteLocationCheck,
        });
      }
    }
   // if condition to check the form fields are empty or contain invalid data
    if (
      fullNameCheck != "" ||
      phoneCheck != "" ||
      emailCheck != "" ||
      imageUrlCheck != "" ||
      summaryCheck != "" ||
      addressCheck != "" ||
      cityCheck != "" ||
      countryCheck != "" ||
      zipcodeCheck !== "" ||
      educationErrors.length > 0
    ) {
      // it prevents the default form submission 
      prevent_default();
      showError = true;
      showMessage = "Please fill all the required details correctly";
      window.scrollTo(0, 0);
    }
    else{
    try{
        const response = await fetch("http://127.0.0.1:8000/new-resume",{
        method: "POST",
        mode : "cors",
        cache : "default",
        headers: {
          "Content-Type":"application/json"
        },
    body: JSON.stringify(formValue)
  });
        const result = await response.json();
        console.log("Success:", result);
        successMessage = "Resume saved successfully!";
        document.getElementById('clear-form').reset();
        window.scrollTo(0, 0);
}
catch(error){
  console.log("Error:",error);
}
console.log(formValue);
  }
}

</script>

<main>
  <form action="" on:submit|preventDefault={submitForm} id="clear-form">
    {#if showMessage}
      <div class="warning-alert">
        <!-- error messages if any fields are invalid -->
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <!-- svelte-ignore a11y-no-static-element-interactions -->
        <span class="closebtn" on:click={() => (showMessage = false)}>&times;</span>
        <!-- svelte-ignore missing-declaration -->
        <p class="error-message">{showMessage}</p>
    </div>
    {/if}

    <!-- svelte-ignore missing-declaration -->
    {#if warningMessage}
      <div class="warning-alert">
          <!-- error messages if any fields are invalid -->
          <!-- svelte-ignore a11y-click-events-have-key-events -->
          <!-- svelte-ignore a11y-no-static-element-interactions -->
          <span class="closebtn" on:click={() => (warningMessage = false)}>&times;</span>
          <!-- svelte-ignore missing-declaration -->
          <p class="error-message">{warningMessage}</p>
      </div>
    {/if}

   <!-- svelte-ignore missing-declaration -->
   {#if successMessage}
        <!-- svelte-ignore missing-declaration -->
    
        <div class="success-alert">
            <!-- error messages if any fields are invalid -->
            <!-- svelte-ignore a11y-click-events-have-key-events -->
            <!-- svelte-ignore a11y-no-static-element-interactions -->
            <span class="closebtn" on:click={() => (successMessage = false)}>&times;</span>
            <!-- svelte-ignore missing-declaration -->
            <p class="success-message">{successMessage}</p>
        </div>
    {/if}

    <div class="back-container">
      <div class="back-icon">
        <Icon icon={arrowLeftIcon} width="24" />
      </div>
      <div class="title">
        <a href="#/list"><h3>Back to All Resumes</h3> </a>
      </div>
    </div>
    <button class="mainheading">
      <h1 class="heading">Resume Details</h1>
      <!-- svelte-ignore a11y-invalid-attribute -->
    </button>
    <PersonalDetails
      bind:full_name
      bind:email
      bind:phone_number
      bind:image_url
      bind:summary
    />
    <AddressDetails
      bind:address_line
      bind:street_name
      bind:city
      bind:zip_code
      bind:country
    />
    <EducationDetails bind:educationDetails />
    <WorkExperienceDetails bind:workExperienceDetails />
    <SkillsDetails bind:skillList />
    <SocialMediaDetails bind:socialMediaDetails />
    <ProjectDetails bind:projectDetails />

    <!-- Save and Cancel Buttons -->
    <div class="formButtons">
      <ButtonInput
        buttonClass="save-button"
        type="submit"
        label="Save"
        icon="fa fa-save"
      />
    <a href="#/list">  <ButtonInput
        buttonClass="cancel-button"
        type="button"
        label="Cancel"
        icon="fa fa-times"
      /></a>
    </div>
  </form>
</main>

<style>
  .mainheading {
    margin-top: 45px;
    width: 100%;
    height:  90px;
    display: flex;
    flex-direction: column;
    padding: 10px; /* Adjust the padding as needed for spacing */
  }

  .heading {
    margin-left:8px;
    font-family: 'Times New Roman', serif;
    top: 0;
    left: 0; /* Remove default margin for the h1 element */
  }

  .formButtons {
    display: flex;
    justify-content: end;
  }
 .error-message{
  margin-left: 60px;
  color:red;
  font-size: 20px;
  height: 13px;
 }
 .warning-alert {
    padding: 8px;
    background-color: #ffe4e1;
    color: rgb(0, 0, 0);
    margin-bottom: 15px;
    text-align: center;
    width: 98%;
    margin-top: 50px;
  }
  .success-message {
    color: #001f02;
    font-size: 12px;
    height: 13px;
    margin-left: 6px;
  }
  .success-alert {
    padding: 8px;
    background-color: #c8fcd3;
    color: rgb(0, 0, 0);
    margin-bottom: 15px;
    text-align: center;
    width: 98%;
    margin-top: 50px;
  }
  .mainheading:hover {
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
  }
  .back-container {
    position: absolute;
    top: 0;
    left: 0;
    display: flex;
    align-items: center;
    cursor: pointer;
  }

  .back-icon {
    color: teal;
    margin-right: 8px;
  }

  .title {
    font-size: 18px;
  }
  h3{
    font-family: 'Times New Roman', serif;
    color:teal;
  }
  .closebtn {
    margin-left: 15px;
    color: rgb(0, 0, 0);
    font-weight: bold;
    float: right;
    font-size: 22px;
    line-height: 20px;
    cursor: pointer;
    transition: 0.3s;
  }
</style>
