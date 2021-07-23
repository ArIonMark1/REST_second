<template>
  
  <authors/>

  <div>
    Data from BackEnd
    {{authors}}
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

  const API_URL ='http://127.0.0.1:8000/authors/'

  export default {
    name: 'App',
    components: {
      Authors,
    },
    data: () => ({
        authors: [],
        Myurls: `${API_URL}`,
      }),
    watch: {
      Myurls: function(url) {
       
          fetch(url)
          .then(response => console.log('Json files is here: ' + response.json() ))
          .then( json => console.log(`Json files is here: ${json}`) )
          .catch(err => alert(err))

          
           
      }
    }

      
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
