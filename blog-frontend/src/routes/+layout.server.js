
export const load = async ({locals}) => {
    if (locals) {
        return {
            user: locals
        }
    }
};