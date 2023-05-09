import { redirect } from "@sveltejs/kit"


export const isTokenExpired = (token) => {
    const expiry = (JSON.parse(atob(token.split(".")[1]))).exp
    // console.log(expiry*1000, Date.now())
    const timeRemaining = expiry * 1000 - Date.now()
    const refreshTime = 60 * 1000
    return timeRemaining <= refreshTime
}

export const logout = (cookies) => {
    cookies.delete("access")
    cookies.delete("refresh")
    console.log("user logged out")
    throw redirect(303, "/login")
}


export const addAuthTokens = (cookies, token, tokenName, timer) => {
    cookies.set(tokenName, token, {
        sameSite: 'strict',
        path: '/',
        httpOnly: true,
        maxAge: timer,
    })
}

