
export const createLoginRedirect = (url: URL) => {
  const redirectedTo = url.searchParams.get("next") || "";
  return `/${redirectedTo.slice(1)}`;
};

