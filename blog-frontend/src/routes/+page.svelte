<script>
    import { page } from "$app/stores";
    import Hero from "../layouts/Hero.svelte";
    let {data: articles} = $page.data
    
</script>

<Hero blogs={articles}></Hero>
