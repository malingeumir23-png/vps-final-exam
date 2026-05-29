const BASE_URL = "http://31.97.191.52:8000";

export async function getProducts() {
  const res = await fetch(`${BASE_URL}/products`);
  return res.json();
}

export async function getOrders() {
  const res = await fetch(`${BASE_URL}/orders`);
  return res.json();
}

export async function getAnalytics() {
  const res = await fetch(`${BASE_URL}/analytics`);
  return res.json();
}
