import { redirect } from '@sveltejs/kit'

export const load = async(request) => {
    const isUser = request.locals.login
    console.log(request.locals, "running create")
    if (!isUser) {
        const pathName = request.url.pathname
        throw redirect(303, `/login?next=${pathName}`)
    }
}