<script>
  import { enhance } from "$app/forms";
  export let form
  let username,
    email,
    password,
    confirmPassword,
    invalidClass,
    passwordsMatch,
    isvalidEmail;

  $: invalidClass = username && username.length > 3 ? "" : "invalid";
  $: passwordsMatch = password === confirmPassword && password;
  $: isvalidEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
</script>

<form method="POST" action="?/register" use:enhance>
  <h2>Create an account</h2>
  <label for="username">Username:</label>
  <input
    class={invalidClass}
    type="text"
    id="username"
    name="username"
    bind:value={username}
  />

  <label for="email">Email:</label>
  <input
    class:invalid={!isvalidEmail}
    bind:value={email}
    type="email"
    id="email"
    name="email"
  />

  <label for="password">Password:</label>
  <input bind:value={password} type="password" id="password" name="password" />

  <label for="confirm-password">Confirm Password:</label>
  <input
    bind:value={confirmPassword}
    type="password"
    id="confirm-password"
    name="confirm-password"
  />
  <p>Passwords match: {passwordsMatch ? "Yes" : "No"}</p>
  {#if form}
    <p>{form.error}</p>
  {/if}

  <button
    class:disabled={invalidClass || !passwordsMatch || !isvalidEmail}
    type="submit">Register</button
  >
</form>

<style>
  form {
    margin: 0 auto;
    width: 50%;
    text-align: center;
  }

  h2 {
    margin-bottom: 30px;
  }

  label {
    display: block;
    margin-bottom: 10px;
    text-align: left;
  }

  input {
    display: block;
    margin-bottom: 20px;
    width: 100%;
    padding: 10px;
    border: none;
    border-radius: 5px;
    background-color: #f5f5f5;
  }

  button[type="submit"] {
    padding: 10px 30px;
    border: none;
    border-radius: 5px;
    background-color: #1abc9c;
    color: #fff;
    cursor: pointer;
    transition: all 0.3s ease;
  }

  button[type="submit"]:hover {
    background-color: #16a085;
  }

  input:focus {
    outline: none;
  }

  .invalid {
    border: 0.5px solid red;
  }
  button.disabled {
    cursor: not-allowed;
    pointer-events: none;
    background-color: rgb(111, 141, 111);
  }
</style>
