<template>
  <main class="container mt-5">
    <div class="row">
      <div class="col-12 text-right mb-4">
        <div class="d-flex justify-content-between">
          <h3>La Recipes</h3>
          <nuxt-link to="/recipes/add" class="btn btn-info">Add Recipe</nuxt-link>
        </div>
      </div>
      <template v-for="recipe in recipes">
        <div :key="recipe.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
          <RecipeCard :onDelete="deleteRecipe" :recipe="recipe"></RecipeCard>
        </div>
      </template>
    </div>
  </main>
</template>

<script>
import RecipeCard from "~/components/RecipeCard.vue";

export default {

  head() {
    return {
      title: "Recipes list"
    };
  },

  components: {
    RecipeCard
  },

  async asyncData({ $axios, params, app}) {

    console.log(app.$auth.loggedIn)
    //console.log(app.$auth.$state);
    //alert(app.$cookies.get("auth._token.local"));

    try {

//$axios.interceptors.request.use(request => {
//  console.log('Starting Request: ', request)
//  return request
//})
	
      let recipes = await $axios.$get(`/recipes/`);
      return { recipes };

    } catch (e) {
      return { recipes: [] };
    }

  },

  data() {
    return {
      recipes: []
    };
  },

  methods: {
    async deleteRecipe(recipe_id) {
      //alert(this.$cookies.get("auth._token.local"));
      try {
        //await this.$axios.$delete(`/recipes/${recipe_id}/`);
        //let newRecipes = await this.$axios.$get("/recipes/");
        //this.recipes = newRecipes;
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>

<style scoped>
</style>
