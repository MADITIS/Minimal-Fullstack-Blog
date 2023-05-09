import { redirect } from '@sveltejs/kit'
import { SERVER_URL } from '$env/static/private';

export const actions = {
    default: async ({request, locals, fetch}) => {
        const formData = await request.formData()
        const user = locals.user.id

        formData.append("author", user)
        console.log("img",formData.get("image"))

        const response = await fetch(`${SERVER_URL}/blogs/create/`, {
            method: "POST",
            body: formData,
        })

        const statusCode = response.status

        switch (statusCode) {
            case 200:
                throw redirect(301, '/')
            case 400:
                console.log("Field Missing")
                break
            case 404:
                console.log("Not logged in/invalid user")
                break
        }       

    }
}