<template>
  
  <authors/>

  <div>
    Data from BackEnd
    {{authors}}
    <br>
    {{ Myurls }}
      <tr v-for="author in authors" :key="author.id">
      <td>DATA</td>
        <td>{{authors}}</td>

        <td>{{author.first_name}}</td>
        <td>{{author.last_name}}</td>
        <td>{{author.birthday_year}}</td>
        
      </tr>
  </div>
  
</template>



<script>
  import Authors from './components/Authors.vue'
  import axios from 'axios'

  const API_URL ='http://127.0.0.1:8000/users/'

  export default {
    name: 'App',
    components: {
      Authors,
    },
    data: () => ({
        authors: [],
        Myurls: `${API_URL}`,
      }),
      mounted() {
        axios
          .get('http://127.0.0.1:8000/users')
          .then(response => response.json())
          .then(json => this.authors = json)
          .catch(err => alert(err))
      },

    // watch: {
    //   Myurls: function(url) {
       
    //     fetch(url)
    //       .then(response => console.log('Json files is here: ' + response.json() ))
    //       .then( json => console.log(`Json files is here: ${json}`) )
    //       .catch(err => alert(err))

          
           
    //   }
    // }

      
  }
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
