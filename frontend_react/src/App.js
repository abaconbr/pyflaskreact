import './App.css';
import React, { useState, useEffect } from 'react';
import ArticleList from './components/ArticleList';
import Form from './components/Form';

function App() {

  const [articles, setArticles] = useState([])
  const [editedArticle, setEditedArticle] = useState(null)

  useEffect(() => {
    fetch('/api/get', {
      method:'GET',
      headers:{
        'Content-Type': 'application/json'
      },
      mode: 'cors'
    })
    .then(response => response.json())
    .then(response => setArticles(response))
    .catch(error => console.log(error))
  }, [])

  const editArticle = (article) => {
    setEditedArticle(article)
  }

  const openForm = () => {
    setEditedArticle({title:'', body:''})
  }

  const updateData = (article) => {
    const newArticle = articles.map(my_article =>{
      if (my_article.id === article.id) {
        return article
      } else {
        return newArticle
      }
    })
    setArticles(newArticle)
  }

  const insertedArticle = (article) => {
    const newArticle = [...articles. article]
    setArticles(newArticle)
  }

  const deletedArticle = (article) => {
    const newArticle = articles.filter(my_article => {
      if (my_article.id === article.id) {
        return false
      }
      return true
    })
    setArticles(newArticle)
  }

  return (
    <div className="App">
        <div className="row">
          <div className="col">
            <h2>Welcome to Flask and ReactJS Full Stack</h2>
          </div>
          <div className="col">
            <button className="btn btn-success"
            onClick={openForm}
            >Create Article</button>
          </div>
        </div>

        <br/>
        <br/>
        <ArticleList articles = {articles} 
        editArticle = {editArticle} 
        deletedArticle = {deletedArticle}
        />

        {editedArticle ? 
        <Form article = {editedArticle} 
        updateData = {updateData} 
        insertedArticle= {insertedArticle} 
        />
        : 
        null}
    </div>
  );
}

export default App;
