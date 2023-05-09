<script>
  import { page } from "$app/stores";
  // import { logout } from "../lib/accountState.js";
  import Button from "./Button.svelte";
  import Logout from "./Logout.svelte";
  import Navbar from "./Navbar.svelte";
  $: user = $page.data.user.login;

  let menuVisible = true
  const showMenu = () => {
    menuVisible = false
  }
</script>

<header class="primary-header flex | p-3">
  <h1 class="primary-title"><a href="/">Expressive Soul</a></h1>
  <Navbar />
  <div class="main-acc left-col flex">
    {#if user}
      <!-- <Logout></Logout> -->
      {#if !$page.url.pathname.startsWith("/create")}
        <a href="/create" class="write user-access"
          ><i class="fa-solid fa-pen" /></a
        >
      {/if}
      <a href="/profile" class="user-account user-access"
        ><i class="fa-solid fa-user" /></a
      >
    {:else}
      <Button buttonType="login">Log in</Button>
      <Button buttonType="register">Sign Up</Button>
    {/if}
  </div>
  <div class="account-tab">
    <ul>
      <li><a href="/profile">Profile</a></li>
      <li><a href="/logout">Logout</a></li>
    </ul>
  </div>
</header>

<style>
  .primary-header {
    position: relative;
  }

  .primary-title {
    font-size: 1.3rem;
  }

  .account-tab {
    /* justify-self: flex-end; */
    position: absolute;
    display: none;
    right: 1rem;
    top: 6rem;
  }

  .user-access {
    cursor: pointer;
    font-size: 1.2rem;
    height: 2.5rem;
    width: 2.5rem;
    /* text-align: center; */
    display: grid;
    place-content: center;
    border-radius: 999px;
    padding: 0.5rem;
    background-color: rgba(246, 202, 69, 0.5);
    transition: all 0.3s ease-in-out;
  }

  .user-access:hover {
    background-color: rgba(246, 202, 69);
  }
</style>
