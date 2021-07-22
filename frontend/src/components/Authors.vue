<template>
  <div>
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

  const API_URL ='http://127.0.0.1:8000/authors/'

  export default {

    data: () => ({

      authors: [],

    }),

    mounted() {
      this.makeGETRequest(`${API_URL}`)
    },

    methods: {
      makeGETRequest(url) {
        fetch(url)
          .then((data) => data.json() )
          .then( (data) => this.authors = data )
      }
      }
    }

</script>


<style>

</style>
