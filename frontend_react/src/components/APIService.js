export default class APIServer {

    static UpdateArticle(id, body) {
        return fetch(`/api/update/${id}`, {
            method:'PUT',
            headers:{
              'Accept': 'application/json',
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(body),
            mode: 'cors'
          })
          .then(resp => resp.json())
    }

    static InsertArticle(body) {
      return fetch(`/api/add`, {
          method:'POST',
          headers:{
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(body),
          mode: 'cors'
        })
        .then(resp => resp.json())
    }

    static DeleteArticle(id) {
      return fetch(`/api/delete/${id}`, {
          method:'DELETE',
          headers:{
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          mode: 'cors'
        })
    }

}

