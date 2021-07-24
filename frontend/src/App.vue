<template>
  
  <authors/>

  <div>
    Data from BackEnd
    <br>
    =================
    <br>

      <div class="table" v-for="book in books" :key="book.id">

        <div class="column" v-for="(v, k) in book" :key="v">

          <p class="title">{{k}}:</p>
          <p class="content">{{v}}</p>
          
        </div>
        <!--{{'='.repeat(268)}} -->
      </div>
        
  </div>
  
</template>

<script>
  import Authors from './components/Authors.vue'
  import axios from 'axios'


  export default {
    name: 'App',
    components: {
      Authors,
    },
    data: () => ({
        urls: null,
        users: null,
        books: null,
        authors: null,
      }),
      mounted() {
        axios
          .get('http://127.0.0.1:8000/books/')
          // .then(response => this.users = response.data)
          .then(data => this.books = data.data)
          .catch(err => alert(err))
      },
      
  }
</script>

<style>
* {
  margin: 0;
  padding: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.title {
  background-color: #619b9e;
  padding: 4px 10px;
}
.content {
  padding: 10px;
}
.table {
    display: flex;
    flex-direction: initial;
    margin-top: 20px;
}
.column {
  display: flex;
  flex-direction: column;
  background-color: #87c6ae;
  border: 1px solid #000;
}
</style>
