import { SERVER_URL } from '$env/static/private';
import { json } from '@sveltejs/kit';

export const DELETE = async({request, fetch, locals}) => {
    const userID = locals.user.id
    const { blogID } = await request.json()
    const response = await fetch(`${SERVER_URL}/blogs/delete/`, {
        method: 'DELETE',
        body: JSON.stringify({
            "blogID": blogID,
            "userID": userID
        }),
        headers: {
            "Content-Type": "application/json"
        },
        
      });
    return json({status: response.status})
}