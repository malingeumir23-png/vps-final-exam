const API_URL = "http://31.97.191.52:8000";

export async function getAnalytics() {
    const response = await fetch(`${API_URL}/analytics`);
    return response.json();
}

export async function getProducts() {
    const response = await fetch(`${API_URL}/products`);
    return response.json();
}

export async function getUsers() {
    const response = await fetch(`${API_URL}/users`);
    return response.json();
}
