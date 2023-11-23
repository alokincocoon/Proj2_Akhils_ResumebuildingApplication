<script>
  export let id = "";
  export let placeholder = "";
  export let label = "";
  export let value;
</script>

<main>
  <div class="inputContent">
    <div class="labelField">
      <label for={id}>{label}</label>
    </div>
    <div class="inputField">
      <input type="url" {id} {placeholder} bind:value />
    </div>
  </div>
</main>

<style>
  .inputContent {
    display: flex;
    border: solid 1px rgb(207, 203, 203);
    height: 45px;
  }
  .inputField:focus-within {
    outline: none;
    border-bottom: 3px solid teal;
  }
  .labelField {
    width: 20%;
    background-color: #f4f6f8;
  }
  label {
    padding-left: 13px;
    padding-top: 10px;
  }
  .inputField {
    height: 38px;
    width: 40%;
    border-bottom: 2px solid #e6e6e6;
    border-radius: 5px; /* Adjust the width and color as needed */
  }
  input[type="url"] {
    height: 38px;
    width: 100%;
    border: none;
    padding: 12px;
    font-size: 1em;
  }
  input[type="url"]:focus {
    outline: none;
  }
</style>
