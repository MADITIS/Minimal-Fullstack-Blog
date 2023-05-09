import { SERVER_URL } from '$env/static/private';
import { isTokenExpired, logout } from './lib/accountState';

export async function handle({event, resolve}) {
    const access = event.cookies.get("access")
    const refresh = event.cookies.get("refresh")
    const user = event.cookies.get("User")

    if (access && isTokenExpired(access)) {
        console.log("refreshing tokens")
        await refreshToken(refresh, event.cookies, event.fetch)
    } else if (!access && refresh) {
        await refreshToken(refresh, event.cookies, event.fetch)
    }

    if (event.url.pathname.startsWith("/logout")) {
        logout(event.cookies)
    }

    if (access) {
        console.log("user logged in")
        event.locals = {
            login: true,
            user:JSON.parse(user),
        } 
    }

    const response = await resolve(event)

    return response
}



const refreshToken = async(oldRefreshToken, cookies, fetch) => {
    const response = await fetch(`${SERVER_URL}/token/login/refresh/`,{
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            refresh: oldRefreshToken
        })
    }).then((value)=> console.log("Success")).catch((err)=> logout(cookies))

    if (!response) {
        logout(cookies)
    }

    if (response.status === 401) {
        logout(cookies)
    }
    const responseData = await response.json()
    console.log("got refresh tokens")
    const {access , refresh} = responseData
    addAuthTokens(cookies, access, "access", 30*60)
    addAuthTokens(cookies, refresh, "refresh", 91*24*60*60)
}

