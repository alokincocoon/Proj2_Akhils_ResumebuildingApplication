<script>
  import MdKeyboardArrowUp from "svelte-icons/md/MdKeyboardArrowUp.svelte";
  import InputField from "../InputFields/InputField.svelte";
  export let open = false;
  import Icon from "@iconify/svelte";
  import { slide } from "svelte/transition";
  import UrlField from "../InputFields/UrlField.svelte";

  const handleClick = () => (open = !open);
  export let socialMediaDetails = [{ network: "", media_name: "", url: "" }];

  const addSocialMedia = () => {
    socialMediaDetails = [
      ...socialMediaDetails,
      { network: "", media_name: "", url: "" },
    ];
  };
  const removeSocialMedia = (index) => {
    if (socialMediaDetails.length > 1) {
      socialMediaDetails = socialMediaDetails.filter((_, i) => i !== index);
    }
  };
</script>

<main>
  <div class="container">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <div class="accordion-class" on:click={handleClick}>
      <h4 class="heading">Social Media Details</h4>
      <div class="custom-icon {open ? 'rotate-down' : ''}">
        <MdKeyboardArrowUp />
      </div>
    </div>
    {#if open}
      {#each socialMediaDetails as Social, i}
        <div class="active" transition:slide>
          <InputField
            placeholder="Add Network"
            label="Network Name"
            id="network name"
            bind:value={Social.network}
          />
          <InputField
            placeholder="Add Media Name"
            label="User Name"
            id="medianame"
            bind:value={Social.media_name}
          />
          <UrlField
            placeholder="Enter the Url"
            label="Url"
            id="urlso"
            bind:value={Social.url}
          />
        </div>
        <div>
          <button class="add-project" on:click|preventDefault={addSocialMedia}
            ><Icon icon="fa-solid:plus" style="margin-right: 8px;" />Add Media</button
          >
          {#if i != 0}
            <button
              class="remove-project"
              on:click|preventDefault={() => removeSocialMedia(i)}
              ><Icon icon="fa-solid:times" style="margin-right: 8px;" />Remove
              Media</button
            >
          {/if}
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
