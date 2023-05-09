<script>
  import { page } from "$app/stores";
  import { createEventDispatcher } from "svelte";
  import Button from "./Button.svelte";
  const dispatch = createEventDispatcher();

  function deletePost(id) {
    dispatch("deletePost", {
      postID: id,
    });
  }
  const pathName = $page.url.pathname
  export let item;
</script>

<article>
  <div class="article__body__left fc-1">
    <div class="article__info flex">
      <div class="flex">
        <div class="author__img">
          <img
            src="https://images.unsplash.com/photo-1680763921539-afae7b2c219e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=763&q=80"
            alt=""
          />
        </div>
        <div class="flex">
          <h2 class="author__name">{item.author.username}</h2>
          <span class="dot" />
          <p class="article__date">{item.date_added}</p>
        </div>
      </div>
      <p class="time_since">3 Hours ago</p>
    </div>
    <div class="ariticle__body flex">
      <div class="article__content fc-3">
        <div class="fc-1">
          <h2 class="article__title">{item.title}</h2>
          <p class="article__description">{item.content}</p>
        </div>
        <ul class="article__categories">
          <li style="background-color: black;">Food</li>
          <li style="background-color: #E5E4E2; color: black;">Nature</li>
        </ul>
        {#if pathName.startsWith("/profile")}
        <button on:click={() => deletePost(item.id)} class="btn other">
          Delete
        </button>
        {/if}
      </div>
      <div class="article_img">
        <img src="http://127.0.0.1:8000{item.image}" alt="" />
      </div>
    </div>
  </div>
</article>

<style>
  article {
    /* display: grid; */
    /* grid-template-columns: 1fr 0.2fr; */
    padding: 1.5rem 2rem;
    border: 1px solid rgba(192, 192, 192, 0.4);
    border-radius: 8px;
  }

  .author__img {
    width: 2.5rem;
    height: 2.5rem;
  }

  .author__img img {
    border-radius: 100vw;
  }

  .ariticle__body {
    --flex-justify: space-between;
    --flex-align: flex-start;
  }

  .article__content {
    flex-basis: 200%;
    /* margin-block-start: 1rem; */
  }

  .article__content div {
    max-width: 80%;
  }

  .article_img {
    flex-basis: 100%;
  }

  .article_img img {
    aspect-ratio: 1/1;
    border-radius: 5px;
  }

  .article__title {
    font-size: 1.2rem;
  }

  .article__description {
    font-size: 0.9rem;
    line-height: 1.7;
  }

  .author__name {
    font-size: 0.8rem;
  }

  .article__date {
    font-size: 0.8rem;
    color: rgb(168, 160, 160);
  }

  .dot {
    width: 3px;
    height: 3px;
    background-color: rgb(0, 0, 0);
    border-radius: 900vw;
  }

  .time_since {
    font-size: 0.8rem;
    color: rgb(48, 47, 47);
  }

  .article__categories {
    display: flex;
    gap: 1.5rem;
    margin-bottom: 2rem;
  }

  .article__categories li {
    /* background-color: #1C82AD; */
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 5px;
    font-size: 0.8rem;
  }

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
