<script>
  export let default_option = "";
  export let options = [];
  export let label = "";
  export let id = "";
  export let value = "";
</script>

<main>
  <div class="selectInput">
    <div class="labelField">
      <label for={id}>{label}</label>
    </div>
    <div class="selectField">
      <select bind:value>
        <option value="">{default_option}</option>
        {#each options as option}
          <option value={option}>{option}</option>
        {/each}
      </select>
    </div>
  </div>
</main>

<style>
  .selectInput {
    display: flex;
    border: solid 1px rgb(207, 203, 203);
    height: 50px;
  }
  .selectInput:focus {
    border-bottom: 1px solid teal;
  }
  .labelField {
    width: 20%;
    background-color: #f4f6f8;
  }
  label {
    padding-left: 13px;
    padding-top: 10px;
  }
  .selectField {
    background-color: white;
    height: 40px;
    width: 40%;
    border-bottom: 2px solid #e6e6e6;
    border-radius: 5px;
  }
  select {
    background-color: white;
    height: 35px;
    width: 100%;
    border: none;
    padding-top: 2px;
    font-size: 1em;
  }
  select::placeholder {
    color: #a9a9a9; /* Light grey color */
  }
  select:focus {
    outline: none;
  }
  select option:first-child {
    display: none;
  }
</style>
