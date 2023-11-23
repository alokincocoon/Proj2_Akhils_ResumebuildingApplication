<script>
  import Router from "svelte-spa-router";
  import ListingPage from "./components/Pages/ListingPage.svelte";
  import ResumeForm from "./components/ResumeDetails/ResumeForm.svelte";
  import Editform from "./EditDetails/Editform.svelte";

  let routes = {
    "/": ResumeForm,
    "/list": ListingPage,
    "/edit" :Editform
  };
</script>

<main>
  <!-- svelte-ignore missing-declaration -->
  <Router {routes} />
</main>
