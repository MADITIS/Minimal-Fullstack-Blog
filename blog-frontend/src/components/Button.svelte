<script>
  export let buttonType;
</script>

<a
  href="/{buttonType}"
  class={buttonType === "login"
    ? "login"
    : buttonType === "other"
    ? "other"
    : "btn"}
>
  <slot />
</a>

<style>
  .login {
    background-color: inherit;
    color: black;
    border: 1px solid silver;
  }
  a,
  .btn {
    padding: 0.5rem 1rem;
    border: none;
    color: white;
    background-color: black;
    border-radius: 5px;
    font-weight: 600;
  }
  .other {
    color: rgb(0, 0, 0);
    background-color: #f6ca45;
  }
</style>
