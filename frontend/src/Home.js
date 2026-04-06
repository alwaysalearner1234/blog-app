import { useEffect, useState } from "react";
import axios from "axios";

function Home() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/posts/")
      .then(res => setPosts(res.data));
  }, []);

  return (
    <div>
      <h1>Blog Posts</h1>
      {posts.map(p => (
        <div key={p.id}>
          <h3>{p.title}</h3>
          <p>{p.content}</p>
        </div>
      ))}
    </div>
  );
}

export default Home;
