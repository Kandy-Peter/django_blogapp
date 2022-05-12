import React from 'react'

const PostCard = ({posts}) => {

  if (!posts || posts.length === 0) return <p>Can not find any posts, sorry</p>;

  return (
    <div className="post-card">
      {posts.map(post => (
        <div className="card">
          <img src="https://source.unsplash.com/random" alt={post.title} />
          <div className="card-descript">
            <h4>{post.title.substr(0, 40)}...</h4>
            <p>{post.excerpt.substr(0, 50)}...</p>
          </div>
        </div>
      ))}
    </div>
  )
}

export default PostCard