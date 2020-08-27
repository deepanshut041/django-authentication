const DashboardPlugin = require("webpack-dashboard/plugin");
const path = require('path');
module.exports = {
	context: __dirname,
	entry: {
		report_dashbord_bundle: ["./root.jsx"]
	},
	output: {
		path: path.resolve("../../webpack_build/", "landing_page"),
		filename: 'landing_page.js',
		library: 'landing_page'
	},
	resolveLoader: {
		moduleExtensions: [path.resolve(__dirname, "node_modules")]
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
				test: /\.css$/,
				use: ['style-loader', 'css-loader'],
			},
			{
				test: /\.(png|j?g|svg|gif)?$/,
				use: 'file-loader'
			}
		]
	},
	plugins: [new DashboardPlugin()]
};