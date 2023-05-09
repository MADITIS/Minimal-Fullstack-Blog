<script>
    // export let cardType = "small"
</script>

<div class="card | p-2">
    <div class="left-card">
        <div class="card-container fc-2">
            <p class="card-type">Food</p>
            <div class="fc-1">
                <h2 class="card-title">Understanding the reasons behind a successful startup</h2>
                <p class="card-overview">
                    Going over the reasons why most successful startups should understand the basics of business instead of just launching into the void without any market study.
                </p>
            </div>
        </div>
    </div>
    <div class="right-card">
        <img src="https://images.unsplash.com/photo-1680676960765-f18115aa7390?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80" alt="">
    </div>
</div>

<style>
    .card {
        display: grid;
        /* grid-template-rows: 1fr; */
        grid-template-columns: 1fr 0.7fr;
        /* height: 20rem; */
    }

    .card-type {
        font-size: 0.8rem;
        /* border: 1px solid silver; */
        text-transform: uppercase;
        background-color: #E5E4E2;
        color: black;
        font-weight: bold;
        /* background-color: white; */
        /* color: black; */
        width: fit-content;
        padding: 0.5rem 1rem;
        border-radius:3px;
    }

    .left-card {
        background: black;
        color: white;
        padding: 1.5rem 2rem;
        flex-basis: 60%;
        /* border-bottom: 1px solid silver; */
    }
    .right-card {
        max-height: 22rem;
    }

    .card-container {
        max-width: 80%;
    }

    .card-title {
        line-height: 1.2;
        font-size: 1.4rem;
        text-transform: capitalize;
        /* color: silver; */
    }
    .card-overview {
        /* font-size: 0.9rem; */
        color: silver;
    }

    
</style>