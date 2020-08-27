const DashboardPlugin = require("webpack-dashboard/plugin");
const path = require('path');

module.exports = {
  context: __dirname,
  entry: {
    report_dashbord_bundle: ["./root.jsx"]
  },
  output: {
    path: path.resolve("../../", "js"),
    filename: 'auth_page.js',
    library: 'auth_page'
  },
  resolveLoader: {
    moduleExtensions: [path.resolve(__dirname, "node_modules")],
  },
  resolve: {
    extensions: ['.js', '.jsx', '.scss',]
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        use: {
          loader: 'babel-loader?cacheDirectory=true',
          options: {
            "presets": [
              "@babel/preset-env",
              "@babel/preset-react"
            ],
          }
        }
      },
      {
        test: /\.module\.s[ac]ss$/i,
        use: ['style-loader', 'css-loader', 'sass-loader'],
      },
      {
        test: /\.(png|j?g|svg|gif)?$/,
        use: 'file-loader'
      }
    ]
  },
  plugins: [new DashboardPlugin()]
};