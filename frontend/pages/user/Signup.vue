<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-md-4">
        <form @submit.prevent="submitRecipe">
          <div class="form-group">
            <label for>User Name</label>
            <input type="text" class="form-control" v-model="signup.username">
          </div>
          <div class="form-group">
            <label for>Password</label>
            <input type="password" class="form-control" v-model="signup.password">
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
      title: "Signup"
    };
  },
  data() {
    return {
      signup: {
        username: "",
        password: ""
      },
    };
  },
  methods: {
    async submitRecipe() {
      try {
	  let formData = new FormData();
	  for (let data in this.signup) {
              formData.append(data, this.signup[data]);
	  }
	  await this.$axios.$post("/auth/users/", formData);
	  this.$router.push("/user/login/");
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>

<style scoped>
</style>
