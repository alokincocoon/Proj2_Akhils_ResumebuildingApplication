<script>
  import DateInput from "../InputFields/DateField.svelte";
  import InputField from "../InputFields/InputField.svelte";
  import MdKeyboardArrowUp from "svelte-icons/md/MdKeyboardArrowUp.svelte";
  import Icon from "@iconify/svelte";
  export let open = false;
  import { slide } from "svelte/transition";

  const handleClick = () => (open = !open);
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

  const addNewEducation = () => {
    educationDetails = [
      ...educationDetails,
      {
        qualification: "",
        course_name: "",
        institute_name: "",
        location: "",
        academic_year_startdate: "",
        academic_year_enddate: "",
      },
    ];
  };
  const removeEducation = (index) => {
    if (educationDetails.length > 1) {
      educationDetails = educationDetails.filter((_, i) => i !== index);
    }
  };
</script>

<main>
  <div class="container">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <div class="accordion-class" on:click={handleClick}>
      <h4 class="heading">Education Details</h4>
      <div class="custom-icon {open ? 'rotate-down' : ''}">
        <MdKeyboardArrowUp />
      </div>
    </div>
    {#if open}
      {#each educationDetails as education, i}
        <div class="active" transition:slide>
          <InputField
            placeholder="Enter Qualification"
            label="Qualification"
            id="qualification"
            bind:value={education.qualification}
          />
          <InputField
            placeholder="Enter Coursename "
            label="Coursename"
            id="coursename"
            bind:value={education.course_name}
          />
          <InputField
            placeholder="Enter Institutename"
            label="InstituteName"
            id="institute"
            bind:value={education.institute_name}
          />
          <InputField
            placeholder="Enter Location"
            label="Location"
            id="location"
            bind:value={education.location}
          />
          <DateInput
            placeholder="Enter Academics Startdate"
            label="Start Date"
            id="startdate"
            bind:value={education.academic_year_startdate}
          />
          <DateInput
            placeholder="Enter Academics Enddate"
            label="EndDate"
            id="enddate"
            bind:value={education.academic_year_enddate}
          />
          <div>
            <button
              class="add-education"
              on:click|preventDefault={addNewEducation}
              ><Icon icon="fa-solid:plus" style="margin-right: 8px;" />Add
              Education</button
            >
            {#if i != 0}
              <button
                class="remove-education"
                on:click|preventDefault={() => removeEducation(i)}
                ><Icon icon="fa-solid:times" style="margin-right: 8px;" />Remove
                Education</button
              >
            {/if}
          </div>
        </div>
      {/each}
    {/if}
  </div>
</main>

<style>
  h4:hover {
    cursor: pointer;
  }
  .heading {
    margin-left: 15px;
  }
  .accordion-class {
    display: flex;
  }

  .container {
    position: relative;
    margin-top: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    border-width: 4px;
    border-radius: 0.5rem;
    border-radius: 0.125rem;
    margin-bottom:12px;

  }
  .container:hover {
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
  }
  .custom-icon {
    transform: rotate(180deg);
    width: 2rem;
    transition: all 0.3s ease;
    color: #cbd5e0;
    position: absolute;
    right: 0;
  }
  .rotate-down {
    transform: rotate(360deg);
  }
  .add-education {
    margin-top: 10px;
    margin-left: 10px;
    background: transparent;
    border: none;
    color: teal;
  }
  .remove-education {
    margin-top: 10px;
    margin-left: 10px;
    background: transparent;
    border: none;
    color: teal;
  }
</style>
