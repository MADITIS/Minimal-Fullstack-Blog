import { SERVER_URL } from '$env/static/private';

export const load = async ({ request, locals, fetch }) => {
    console.log("fetching user blogs")

    const userID = locals.user.id
    console.log(userID)

    const fetchBlogs = async () => {
        try {
            const response = await fetch(`${SERVER_URL}/blogs/${userID}/blogs`, {
              method: "GET",
            });
            if (response.status !== 200) {
              throw new Error("Bad/No response Response", {
                cause: response,
              });
            }
            console.log(response.status)
            const data = await response.json();
            
            return data.data
          } catch (err) {
            console.log(err.message)
            return []
          }
    }
    
    return  {
        userBlogs: fetchBlogs()
    }
}
