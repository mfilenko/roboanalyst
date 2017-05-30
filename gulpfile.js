var gulp = require('gulp');
var less = require('gulp-less');
var watch = require('gulp-watch');
var path = require('path');

gulp.task('less', function () {
  return gulp.src('./static/less/main.less')
    .pipe(less({
      paths: [ path.join(__dirname, 'less', 'includes') ]
    }))
    .pipe(gulp.dest('./static/css'));
});

gulp.task('watch', function() {
    gulp.watch('./static/**/*.less', ['less']);  // Watch all the .less files, then run the less task
});
