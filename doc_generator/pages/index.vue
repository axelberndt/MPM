<template>
  <main
    class="container px-12 pt-4 pb-8 mx-auto mb-5 -mt-10 overflow-hidden bg-white shadow-lg sm:rounded-lg"
  >
    <div v-html="content" class="text-sm"></div>
  </main>
</template>

<script>
export default {
  name: "Home",
  data: function() {
    return {
      content: null
    };
  },
  created() {
    let data = require("~/assets/data.json");
    this.content = data.chapters[0];
  }
};
</script>
