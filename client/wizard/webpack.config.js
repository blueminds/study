module.exports = {
  entry: {
    main: './scripts.js',
  },
  output: {
    path: __dirname,
    filename: 'scripts.min.js',
  },
  resolve: {
    extensions: ['', '.webpack.js', '.web.js', '.ts', '.js']
  },
  module: {
    loaders: [
      {
        test: /\.ts$/,
        loader: 'typescript-loader?typescriptCompiler=jsx-typescript'
      }
    ]
  }
};
