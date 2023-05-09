<script>
    import { page } from "$app/stores";
    import Article from "../../../components/Article.svelte";
    let {userBlogs} = $page.data
    const userID = $page.data.user.user.id
    console.log($page)
    let articles = userBlogs.data
    const deletePost = async (event) => {
        const blogID = event.detail.postID
        const response = await fetch("/profile", {
            method: 'DELETE',
            headers: {
                'Content-Type': "application/json"
            },
            body: JSON.stringify(
                {
                    'blogID': blogID
                }
            )
        })
        if (response.status === 200) {
            articles = articles.filter((article) => article.id !== blogID)
        } else {
            console.log("Can't delete post")
        }
    }
</script>
<div class="profile-container">
    <div class="articles fc-2 pb-5">
    {#if articles}
        {#each articles as blog}
            <Article on:deletePost={deletePost} item={blog}></Article>
        {/each}
    {:else}
    <h3>No Posts</h3>
    {/if}
    </div>
    <aside>
        <ul class="profile-list fc-3">
            <li class="active"><a href="/posts">Posts</a></li>
            <li><a href="/create">Create</a></li>
            <li><a href="/logout">Logout</a></li>
        </ul>
    </aside>
</div>

<style>
    .profile-container {
        display: flex;
        gap: 2rem;
        justify-content: center;
        align-items: center;

    }

    .articles {
        flex-basis:70%;

    }

    aside {
        flex-basis: 30%;
        font-weight: 600;
        text-transform: uppercase;
        background-color: rgba(192, 192, 192, 0.2);
        padding: 2rem;
        border-radius: 5px;
        max-height: 18rem;
        align-self: flex-start;
    }
    
    aside li {
        padding: 0.5rem;
    }
    
    .active {
        color: white;
        background-color: rgb(0, 0, 0);
        border-radius: 5px;
    }
</style>