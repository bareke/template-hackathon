<template>
  <div
    class="flex justify-center mt-56 bg-blue-200 w-1/2 h-32 rounded-xl p-8 justify-between text-3xl"
  >
    <vs-button type="filled" @click="testAPI">Vuexas test</vs-button>
    <span>Box icons funcionando</span>
    <box-icon name="music"></box-icon>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
  mounted() {},

  methods: {
    testAPI() {
      this.$apollo
        .query({ query: require("@/graphql/HelloWorld.gql") })
        .then((response) => {
          console.log(response);
        });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
