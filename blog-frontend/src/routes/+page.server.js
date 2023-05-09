import { SERVER_URL } from '$env/static/private';

export async function load({fetch}) {
  // console.log(request)

    const fetchBlogs = async () => {
        try {
            const response = await fetch(`${SERVER_URL}/blogs`, {
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

    return {
        data: fetchBlogs(),
    }
}
