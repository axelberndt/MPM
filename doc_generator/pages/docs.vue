<template>
  <main
    class="container mx-auto mb-5 -mt-10 overflow-hidden bg-white shadow-lg sm:rounded-lg"
  >
    <div class="p-5">
      <div
        class="flex items-center w-full px-3 py-2 border border-gray-400 rounded-lg bg-gray-50"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="w-5 h-5 text-gray-500"
          viewBox="0 0 512 512"
        >
          <path
            fill="currentColor"
            d="M479.968 0H32.038C3.613 0-10.729 34.487 9.41 54.627L192 237.255V424a31.996 31.996 0 0010.928 24.082l64 55.983c20.438 17.883 53.072 3.68 53.072-24.082V237.255L502.595 54.627C522.695 34.528 508.45 0 479.968 0zM288 224v256l-64-56V224L32 32h448L288 224z"
          />
        </svg>
        <input
          v-model="filterString"
          class="w-full ml-2 focus:outline-none bg-gray-50"
          placeholder="Filter..."
        />
      </div>
    </div>
    <div class="overflow-y-auto" @click="onClick">
      <mpm-item
        v-for="item in items"
        :key="item.ident"
        :data="item"
        v-show="
          filterString
            .toLowerCase()
            .split(' ')
            .every(s => item.ident.toLowerCase().includes(s))
        "
        :ref="item.ident"
        :id="item.ident"
      ></mpm-item>
    </div>
  </main>
</template>

<script>
import MpmItem from "../components/MpmItem.vue";

export default {
  name: "app",
  components: {
    MpmItem
  },
  data: function() {
    return {
      filterString: "",
      items: []
    };
  },
  methods: {
    onClick: function(event) {
      const element = this.$refs[event.target.innerText];
      if (element && event.srcElement.href) {
        this.filterString = "";
        element[0].isOpen = true;
      }
    }
  },
  created() {
    let data = require("~/assets/data.json");
    this.items = data.items;
  },
  mounted() {
    const hash = this.$router.currentRoute.hash;
    const element = this.$refs[hash.substr(1)];
    if (element) {
      element[0].isOpen = true;
      this.$scrollTo(hash);
    }
  }
};
</script>
