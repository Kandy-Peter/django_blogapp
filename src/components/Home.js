import React, { useState, useEffect } from 'react';
import PostCard from './PostCard';
import PostLoadingComponent from './PostLoading';

const Home = () => {
    const PostLoading = PostLoadingComponent(PostCard);
    const [appState, setAppState] = useState({
      loading: false,
      posts: null,
    });

    useEffect(() => {
      setAppState({ loading: true });
      const apiUrl = `http://127.0.0.1:8000/api/`;
      fetch(apiUrl)
        .then((data) => data.json())
        .then((posts) => {
          setAppState({ loading: false, posts: posts });
        });
    }, [setAppState]);
    return (
      <div className="home-clm">
        <h1>Latest Posts</h1>
        <PostLoading isLoading={appState.loading} posts={appState.posts} />
      </div>
    );
}

export default Home
