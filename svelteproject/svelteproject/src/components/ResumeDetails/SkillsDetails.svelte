<script>
  // font-icon
  import MdKeyboardArrowUp from "svelte-icons/md/MdKeyboardArrowUp.svelte";
  import Icon from "@iconify/svelte";
  import InputField from "../InputFields/InputField.svelte";
  import SelectInput from "../InputFields/SelectField.svelte";
  export let selectSkillLevel = [
    "Expert",
    "Advanced",
    "Intermediate",
    "Beginner",
  ];
  export let open = false;
  import { slide } from "svelte/transition";

  const handleClick = () => (open = !open);

  export let skillList = [{ skill: "", skill_level: "" }];
  const addNewSkill = () => {
    skillList = [...skillList, { skill: "", skill_level: "" }];
  };
  const removeSkill = (index) => {
    if (skillList.length > 1) {
      skillList = skillList.filter((_, i) => i !== index);
    }
  };
</script>

<main>
  <div class="container">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <div class="accordion-class" on:click={handleClick}>
      <h4 class="heading">Skill Details</h4>
      <div class="custom-icon {open ? 'rotate-down' : ''}">
        <MdKeyboardArrowUp />
      </div>
    </div>

    {#if open}
      {#each skillList as skill, i}
        <div class="active" transition:slide>
          <InputField
            placeholder="Enter Skills"
            label="Skills"
            id="skills"
            bind:value={skill.skill}
          />
          <SelectInput
            label="Skill Level"
            options={selectSkillLevel}
            default_option="Add skill level"
            bind:value={skill.skill_level}
          />
          <div>
            <button class="add-education" on:click|preventDefault={addNewSkill}
              ><Icon icon="fa-solid:plus" style="margin-right: 8px;" />Add Skill</button
            >
            {#if i != 0}
              <button
                class="remove-education"
                on:click|preventDefault={() => removeSkill(i)}
                ><Icon icon="fa-solid:times" style="margin-right: 8px;" />Remove
                Skill</button
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
