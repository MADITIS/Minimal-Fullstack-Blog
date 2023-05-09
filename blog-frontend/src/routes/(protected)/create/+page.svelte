<script>
  import { enhance } from "$app/forms";
  let previewIMG = null;
  // let currentIMG = "/src/lib/public/default.jpg"

  const getTheIMG = (event) => {
    const { files } = event.target;
    if (files.length > 0) {
      console.log(files);
      previewIMG = URL.createObjectURL(files[0]);
    }
  };

  let title, content, image;
</script>

<div class="blog-create-form">
  <form
    use:enhance
    action=""
    method="post"
    class="form-group fc-3"
    enctype="multipart/form-data"
  >
    <div class="preview">
      <img src={previewIMG} alt="" />
      <input
        type="file"
        accept="image/*"
        alt="blog image"
        on:change={getTheIMG}
        bind:value={image}
        name="image"
      />
    </div>
    <div class="title-group">
      <input type="text" name="title" placeholder="Title" bind:value={title} />
      <button class:disabled={!title || !content || !image} class="btn save" type="submit"
        >Save</button
      >
    </div>
    <!-- <div class="content-group fc-1"> -->
    <textarea
      placeholder="Content"
      name="content"
      id=""
      cols="30"
      rows="10"
      bind:value={content}
    />
    <!-- <div class="blog-img">
        <div>
          <label for="bimg">Upload Cover</label>
          <input
            type="file"
            accept="image/*"
            alt="blog image"
            on:change={getTheIMG}
          />
        </div>
      </div> -->
    <!-- </div> -->
  </form>
</div>

<style>
  .preview {
    display: grid;
    place-content: center;
    border: 1px silver dotted;
    padding: 1rem;
    background-color: rgb(241, 239, 239, 0.1);
    border-radius: 5px;
  }
  .preview img {
    max-height: 22rem;
    border-radius: inherit;
  }

  .form-group {
    max-width: 70%;
  }

  .disabled {
    cursor: not-allowed;
    pointer-events: none;
    background-color: rgb(111, 141, 111);
  }

  .title-group {
    display: flex;
    justify-content: space-between;
  }

  .title-group input {
    flex-basis: 85%;
    border-radius: 5px;
    padding-inline: 1rem;
    padding-block: 0.5rem;
  }

  textarea {
    max-width: 100%;
    width: 100%;
    border: none;
    border: 1px solid silver;
    padding: 1rem;
    border-radius: 5px;
  }

  button {
    background-color: inherit;
    color: black;
    border: 1px solid silver;
  }

  button {
    padding: 0.5rem 1rem;
    border: none;
    color: white;
    background-color: black;
    border-radius: 5px;
    font-weight: 600;
  }
</style>
