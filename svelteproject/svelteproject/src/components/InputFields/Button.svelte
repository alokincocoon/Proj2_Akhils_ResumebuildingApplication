<script>
  export let buttonClass = "";
  export let type = "";
  export let label = "";
  export let icon = "";
</script>

<main>
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
  />
  <div class="button-container">
    <button class={buttonClass} {type}
      >{label}<i class={icon} style="margin-left: 8px;" />
    </button>
  </div>
</main>

<style>
  /* Button Styles */
  .button-container {
    margin-top: 20px;
  }
  .save-button {
    background-color: teal; /* Green background color for save button */
    color: white; /* White text color */
    padding: 10px 15px; /* Padding for the button */
    border: none; /* No border */
    border-radius: 5px; /* Rounded corners */
    cursor: pointer; /* Cursor style on hover */
    margin-right: 10px;
  }

  .cancel-button {
    background-color: white; /* Green background color for save button */
    color: teal; /* White text color */
    padding: 10px 15px; /* Padding for the button */
    border: 2px solid teal; /* No border */
    border-radius: 5px; /* Rounded corners */
    cursor: pointer;
  }
</style>
