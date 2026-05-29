import { useEffect, useState } from "react";
import { getAnalytics, getProducts } from "./services/api";

function App() {

  const [analytics, setAnalytics] = useState({});
  const [products, setProducts] = useState([]);

  useEffect(() => {

    async function loadData() {

      const analyticsData = await getAnalytics();
      const productData = await getProducts();

      setAnalytics(analyticsData);
      setProducts(productData);
    }

    loadData();

  }, []);

  return (
    <div style={{padding:"30px"}}>

      <h1>E-Commerce Dashboard</h1>

      <h2>Analytics</h2>

      <p>Total Orders: {analytics.total_orders}</p>

      <p>Total Revenue: ₱{analytics.total_revenue}</p>

      <p>Top Product: {analytics.top_product}</p>

      <h2>Products</h2>

      {products.map(product => (

        <div key={product.id}>
          {product.name} - ₱{product.price}
        </div>

      ))}

    </div>
  );
}

export default App;
