import { SERVER_URL } from '$env/static/private';
import { redirect } from '@sveltejs/kit';

export const actions = {
    register: async ({ cookies, request, fetch }) => {
        const data = await request.formData()
        const fromData = {
            username: data.get("username"),
            email: data.get("email"),
            password: data.get("password")
        }

        try {

            const response = await fetch(`${SERVER_URL}/users/create/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(fromData)
            })

            if (response.status === 409) {
                return {
                    status: false,
                    error: "User already exists",
                    data: Object.fromEntries(data)
                }
            }

            throw redirect(303, "/login")



        } catch (err) {
            if (err instanceof Error) {

                console.log(err.message)
            } else {
                throw err
            }

        }
        // console.log(response)
    }
}