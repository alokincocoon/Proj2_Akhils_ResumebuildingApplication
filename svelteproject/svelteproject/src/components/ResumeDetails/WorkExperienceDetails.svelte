<script>
  import MdKeyboardArrowUp from "svelte-icons/md/MdKeyboardArrowUp.svelte";
  import Icon from "@iconify/svelte";
  import DateInput from "../InputFields/DateField.svelte";
  import InputField from "../InputFields/InputField.svelte";
  export let open = false;
  import { slide } from "svelte/transition";
  const handleClick = () => (open = !open);
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

  const addWorkExperience = () => {
    workExperienceDetails = [
      ...workExperienceDetails,
      {
        job_title: "",
        organization: "",
        job_location: "",
        job_key_role: "",
        job_start_date: "",
        job_end_date: "",
      },
    ];
  };
  const removeWorkExperience = (index) => {
    if (workExperienceDetails.length > 1) {
      workExperienceDetails = workExperienceDetails.filter(
        (_, i) => i !== index
      );
    }
  };
</script>

<main>
  <div class="container">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <div class="accordion-class" on:click={handleClick}>
      <h4 class="heading">Work Experience Details</h4>
      <div class="custom-icon {open ? 'rotate-down' : ''}">
        <MdKeyboardArrowUp />
      </div>
    </div>
    {#if open}
      {#each workExperienceDetails as workexperience, i}
        <div class="active" transition:slide>
          <InputField
            placeholder="Enter Job Title"
            label="Job Title"
            id="job-title"
            bind:value={workexperience.job_title}
          />
          <InputField
            placeholder="Enter Organization"
            label="Organization"
            id="organization"
            bind:value={workexperience.organization}
          />
          <InputField
            placeholder="Enter Job location"
            label="Job Location"
            id="job-location"
            bind:value={workexperience.job_location}
          />
          <InputField
            placeholder="Enter the Keyroles"
            label="Key Roles"
            id="keyroles"
            bind:value={workexperience.job_key_role}
          />
          <DateInput
            placeholder=""
            label="Start Date"
            id="job_start_date"
            bind:value={workexperience.job_start_date}
          />
          <DateInput
            placeholder=""
            label="End Date"
            id="job_end_date"
            bind:value={workexperience.job_end_date}
          />
          <div>
            <button class="add-work" on:click|preventDefault={addWorkExperience}
              ><Icon icon="fa-solid:plus" style="margin-right: 8px;" />Add Work
              Experience</button
            >
            {#if i != 0}
              <button
                class="remove-work"
                on:click|preventDefault={() => removeWorkExperience(i)}
                ><Icon icon="fa-solid:times" style="margin-right: 8px;" />Remove
                Work Experience</button
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
  .heading {
    margin-left: 15px;
  }
  .add-work {
    margin-top: 10px;
    margin-left: 10px;
    background: transparent;
    border: none;
    color: teal;
  }
  .remove-work {
    margin-top: 10px;
    margin-left: 10px;
    background: transparent;
    border: none;
    color: teal;
  }
</style>
