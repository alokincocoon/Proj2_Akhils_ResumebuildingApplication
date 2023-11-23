<script>
  import InputField from "../InputFields/InputField.svelte";
  import MdKeyboardArrowUp from "svelte-icons/md/MdKeyboardArrowUp.svelte";
  import Icon from "@iconify/svelte";
  export let open = false;
  import { slide } from "svelte/transition";

  const handleClick = () => (open = !open);
  export let projectDetails = [
    { project_name: "", project_description: "", skills: "" },
  ];

  const addProject = () => {
    projectDetails = [
      ...projectDetails,
      { project_name: "", project_description: "", skills: "" },
    ];
  };
  const removeProject = (index) => {
    if (projectDetails.length > 1) {
      projectDetails = projectDetails.filter((_, i) => i !== index);
    }
  };
</script>

<main>
  <div class="container">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <div class="accordion-class" on:click={handleClick}>
      <h4 class="heading">Project Details</h4>
      <div class="custom-icon {open ? 'rotate-down' : ''}">
        <MdKeyboardArrowUp />
      </div>
    </div>
    {#if open}
      {#each projectDetails as project, i}
        <div class="active" transition:slide>
          <InputField
            placeholder="Enter Project Name"
            label="Project Name"
            id="project_name"
            bind:value={project.project_name}
          />
          <InputField
            placeholder="Project Description"
            label="Project Description"
            id="project_description"
            bind:value={project.project_description}
          />
          <InputField
            placeholder="Enter Skills"
            label="Skills"
            id="skills"
            bind:value={project.skills}
          />
          <div>
            <button class="add-project" on:click|preventDefault={addProject}
              ><Icon icon="fa-solid:plus" style="margin-right: 8px;" />Add
              Project</button
            >
            {#if i != 0}
              <button
                class="remove-project"
                on:click|preventDefault={() => removeProject(i)}
                ><Icon icon="fa-solid:times" style="margin-right: 8px;" />Remove
                Project</button
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
  .add-project {
    margin-top: 10px;
    margin-left: 10px;
    background: transparent;
    border: none;
    color: teal;
  }
  .remove-project {
    margin-top: 10px;
    margin-left: 10px;
    background: transparent;
    border: none;
    color: teal;
  }
</style>
