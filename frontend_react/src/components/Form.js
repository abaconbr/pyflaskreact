import React, { useState, useEffect } from 'react';
import APIService from './APIService';

function Form(props) {

  const [title, setTitle] = useState('')
  const [body, setBody] = useState('')

  useEffect(() => {
    setTitle(props.article.title)
    setBody(props.article.body)
  },[props.article])

  const updateArticle = () => {
    APIService.UpdateArticle(props.article.id, {title, body})
    .then(resp => props.updateData(resp))
    .catch(err => console.log(err))
  }

  const insertArticle = () => {
    APIService.InsertArticle({title, body})
    .then(resp => props.insertedArticle(resp))
    .catch(err => console.log(err))
  }
  
  return (
    <div>
        {props.article ? (
            <div className="mb-3">
                <label htmlFor = "title" className="form-label">Title</label>
                <input id="title" name="title" type="text" 
                value={title}
                onChange={(e)=> setTitle(e.target.value)}
                className="form-control" 
                placeholder = "Please Enter Title" />

                <label htmlFor = "body" className="form-label">Description</label>
                <textarea id="body" name="body" 
                value={body}
                onChange={(e)=> setBody(e.target.value)}
                row = "5"
                className="form-control" placeholder = "Please Enter Description" />

                {
                  props.article.id ? 
                  <button 
                  className="btn btn-success mt-3"
                  onClick={updateArticle}
                  >Update</button>
                  :
                  <button 
                  className="btn btn-success mt-3"
                  onClick={insertArticle}
                  >Insert</button>
                }

            </div>

        ): null}
    </div>
  )
}

export default Form
