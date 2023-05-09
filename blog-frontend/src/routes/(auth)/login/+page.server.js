import { addAuthTokens } from '$lib/accountState.js'
import { createLoginRedirect } from '$lib/utils.ts'
import { redirect } from '@sveltejs/kit'
import { SERVER_URL } from '$env/static/private';

export const actions = {
    default: async ({cookies, request, url, fetch}) => {
        const data = await request.formData()
        const [email, password] = [data.get("email"), data.get("password")]

        const response = await fetch(`${SERVER_URL}/users/login/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email,
                password
            })
        })
        if (response.status !== 200) {
            throw redirect(303, "/login")
        }
        const responseData = await response.json()
        const {access , refresh} = responseData.data.tokens

        const user = responseData.data.user

        cookies.set("User", JSON.stringify(user))

        addAuthTokens(cookies, access, "access", 30*60)
        addAuthTokens(cookies, refresh, "refresh", 91*24*60*60)
        
        const redirectURL = createLoginRedirect(url)
        throw redirect(302, redirectURL)

    }
}