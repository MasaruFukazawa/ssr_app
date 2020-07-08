<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-md-4">
        <form @submit.prevent="submitRecipe">
          <div class="form-group">
            <label for>User Name</label>
            <input type="text" class="form-control" v-model="login.username">
          </div>
          <div class="form-group">
            <label for>Password</label>
            <input type="password" class="form-control" v-model="login.password">
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  auth: false,
  head() {
    return {
      title: "Login"
    };
  },
  data() {
    return {
      login: {
        username: "",
        password: ""
      },
    };
  },
  methods: {
    async submitRecipe() {
      try {
          await this.$auth.login({data: this.login});
	  this.$router.push("/recipes/");
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>

<style scoped>
</style>
