<script>
    import Button from "../components/Button.svelte";
    import Card from "../components/Card.svelte";
// import Login from "../components/login.svelte";
    import Article from "../components/Article.svelte";
    export let blogs
  
</script>
  
  
  <section class="main">
    <div class="hero__main container">
      <div class="left p-5">
        <div class="hero__header flex">
          <h2 class="hero-title">Article Of The Day</h2>
          <!-- <button class="hero__button">View More</button> -->
          <Button buttonType="other">View More</Button>
        </div>
        <Card />
        <div class="articles fc-2 pb-5">
          {#each blogs as blog}
              <Article item={blog} />
          {/each}
        </div>
      </div>
      <div class="p-5 fc-1 aside">
        <div class="newsletter fc-1">
          <h3>Get Blessings Daily</h3>
          <p>Subscribe Now</p>
          <Button buttonType="other">Get Access</Button>
        </div>
        <div class="recommendation">
          <h3>People You Might Be Interested In.</h3>
        </div>
      </div>
    </div>
  </section>
  
  <style>
    .hero-title {
      text-transform: capitalize;
      font-size: 1.2rem;
    }
  
    .main {
      border-top: 1px solid silver;
      /* border: 1px red solid; */
    }
  
    .hero__main {
      /* position: sticky; */
      /* top: 0; */
      display: grid;
      grid-template-columns: 1fr 0.3fr;
      /* gap: 2rem; */
      /* border: 1px red solid; */
    }
    .left {
      border-right: 1px solid silver;
      padding-inline-end: 2rem;
    }
  
    .newsletter {
      background-color: rgba(192, 192, 192, 0.2);
      padding: 1rem 2rem;
    }
    .aside {
      padding-inline-start: 2rem;
      /* position: sticky; */
      /* top: 0; */
    }
  
    .articles {
      border-top: 1px solid silver;
    }
  </style>
  