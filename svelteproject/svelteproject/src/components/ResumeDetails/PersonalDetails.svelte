<script>
  import MdKeyboardArrowUp from "svelte-icons/md/MdKeyboardArrowUp.svelte";
  import EmailInput from "../InputFields/EmailField.svelte";
  import InputField from "../InputFields/InputField.svelte";
  import UrlInput from "../InputFields/UrlField.svelte";
  export let open = false;
  import { slide } from "svelte/transition";
  import { validateFullName } from "../validation";
  import { validatePhone } from "../validation";
  import { validateEmail } from "../validation";
  import { validateImageUrl } from "../validation";
  import { validateSummary } from "../validation";

  const handleClick = () => (open = !open);

  export let full_name = "";
  export let email = "";
  export let phone_number = "";
  export let image_url = "";
  export let summary = "";
</script>

<main>
  <div class="container">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <div class="accordion-class" on:click={handleClick}>
      <h4 class="heading">Basic Details</h4>
      <div class="custom-icon {open ? 'rotate-down' : ''}">
        <MdKeyboardArrowUp />
      </div>
    </div>
    {#if open}
      <div class="active" transition:slide>
        <InputField
          placeholder="Enter your Full Name"
          label="Name"
          id="full_name"
          bind:value={full_name}
        />
        <div class="warning">
          {full_name && validateFullName(full_name)}
        </div>
        <EmailInput
          placeholder="Enter your Email"
          label="Email"
          id="email"
          bind:value={email}
        />
        <div class="warning">
          {email && validateEmail(email)}
        </div>
        <InputField
          placeholder="Enter your Phone Number"
          label="Phone Number"
          id="phone_number"
          bind:value={phone_number}
        />
        <div class="warning">
          {phone_number && validatePhone(phone_number)}
        </div>
        <UrlInput
          placeholder="Enter Image URL"
          label="Image URL"
          id="image_url"
          bind:value={image_url}
        />
        <div class="warning">
          {image_url && validateImageUrl(image_url)}
        </div>
        <InputField
          placeholder="Summary"
          label="Summary"
          id="summary"
          bind:value={summary}
        />
        <div class="warning">
          {summary && validateSummary(summary)}
        </div>
      </div>
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
  .warning {
    color: #ff3860;
    font-size: 12px;
    margin-left: 6px;
  }
</style>
