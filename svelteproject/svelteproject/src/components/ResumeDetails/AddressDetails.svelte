<script>
  import InputField from "../InputFields/InputField.svelte";
  import SelectInput from "../InputFields/SelectField.svelte";
  import MdKeyboardArrowUp from "svelte-icons/md/MdKeyboardArrowUp.svelte";
  import { validateAddress, validateCountry } from "../validation";
  import { validateCity } from "../validation";
  import { validateState } from "../validation";
  import { validateZipcode } from "../validation";
  export let selectCountry = [
    "Australia",
    "Argentina",
    "Canada",
    "Brazil",
    "China",
    "India",
    "Zimbave",
  ];
  export let open = false;
  import { slide } from "svelte/transition";
  const handleClick = () => (open = !open);

  export let address_line = "";
  export let street_name = "";
  export let city = "";
  export let zip_code = "";
  export let country = "";
</script>

<main>
  <div class="container">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <div class="accordion-class" on:click={handleClick}>
      <h4 class="heading">Address</h4>
      <div class="custom-icon {open ? 'rotate-down' : ''}">
        <MdKeyboardArrowUp />
      </div>
    </div>
    {#if open}
      <div class="active" transition:slide>
        <InputField
          placeholder="Add Address"
          label="Address Line"
          id="address"
          bind:value={address_line}
        />
        <div class="warning">
          {address_line && validateAddress(address_line)}
        </div>
        <InputField
          placeholder="Add Street Name"
          label="Street Name"
          id="street_name"
          bind:value={street_name}
        />
        <div class="warning">
          {street_name && validateState(street_name)}
        </div>
        <InputField
          placeholder="Add City"
          label="City"
          id="city"
          bind:value={city}
        />
        <div class="warning">
          {city && validateCity(city)}
        </div>
        <InputField
          placeholder="Add Zipcode"
          label="Zipcode"
          id="zipcode"
          bind:value={zip_code}
        />
        <div class="warning">
          {zip_code && validateZipcode(zip_code)}
        </div>
        <SelectInput
          label="Country"
          options={selectCountry}
          default_option="Choose your country"
          bind:value={country}
        />
        <div class="warning">
          {country && validateCountry(country)}
        </div>
      </div>
    {/if}
  </div>
</main>

<style>
  .heading {
    margin-left: 15px;
  }

  h4:hover {
    cursor: pointer;
  }
  .accordion-class {
    display: flex;
  }

  .container {
    position: relative;
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
  .warning {
    color: #ff3860;
    font-size: 12px;
    margin-left: 6px;
  }
</style>
