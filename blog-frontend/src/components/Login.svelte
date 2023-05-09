<script>
  import { enhance } from '$app/forms';
</script>

<div class="login-page">
    <div class="form">
      <div class="login">
        <div class="login-header">
          <h3>LOGIN</h3>
          <p>Please enter your credentials to login.</p>
        </div>
      </div>
      <form method="POST" use:enhance class="login-form">
        <input name="email" type="text" placeholder="email"/>
        <input name="password" type="password" placeholder="password"/>
        <button>login</button>
        <p class="message">Not registered? <a href="#">Create an account</a></p>
      </form>
    </div>
  </div>


  <style>
    .login-page {
  width: 360px;
  padding: 8% 0 0;
  margin: auto;
}

.form {
  position: relative;
  z-index: 1;
  background: #FFFFFF;
  max-width: 360px;
  margin: 0 auto 100px;
  padding: 45px;
  text-align: center;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
}

.login-form input {
  font-family: 'Roboto', sans-serif;
  outline: 0;
  background: #f2f2f2;
  width: 100%;
  border: 0;
  margin: 0 0 15px;
  padding: 15px;
  box-sizing: border-box;
  font-size: 14px;
}

.login-form button {
  font-family: 'Roboto', sans-serif;
  text-transform: uppercase;
  outline: 0;
  background: #4CAF50;
  width: 100%;
  border: 0;
  padding: 15px;
  color: #FFFFFF;
  font-size: 14px;
  cursor: pointer;
}

.login-form button:hover, .login-form button:active {
  background: #43A047;
}

.message {
  margin: 15px 0 0;
  color: #b3b3b3;
  font-size: 12px;
}

.message a {
  color: #4CAF50;
  text-decoration: none;
}
  </style>