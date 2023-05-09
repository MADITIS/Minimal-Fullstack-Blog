import { redirect } from '@sveltejs/kit'

export function load(request) {

    const redirectPath = request.locals.currentPath || '/'
    console.log("redirectPath", request.locals)
    if (request.locals.login) {
        throw redirect(302, redirectPath)
    }
}

