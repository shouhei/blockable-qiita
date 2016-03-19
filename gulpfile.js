var gulp = require('gulp');
var browserify = require('browserify');
var babelify = require('babelify');
var source = require('vinyl-source-stream');

gulp.task('browserify', function() {
  browserify('./js/app.jsx', { debug: true })
    .transform(babelify, {presets: ["es2015", "react"]})
    .bundle()
    .on("error", function (err) { console.log("Error : " + err.message); })
    .pipe(source('bundle.js'))
    .pipe(gulp.dest('./static/js'))
});

gulp.task('watch', function() {
  gulp.watch('./js/*.jsx', ['browserify'])
});


gulp.task('default', ['browserify', 'watch']);
