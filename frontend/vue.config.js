const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
  pwa: {
    name: "Hackathon",
    themeColor: "#f2f2f2",
    msTileColor: "#000",
    workboxPluginMode: "GenerateSW",
    workboxOptions: {
      skipWaiting: true,
    },
  },
});
