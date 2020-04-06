const path = require('path')
module.exports = {
  'transpileDependencies': [
    'vuetify'
  ],
  publicPath: './',
  outputDir: path.resolve(__dirname, '../back/templates'),
  assetsDir: 'static'
}
