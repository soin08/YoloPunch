'use strict';

// Include Gulp & Tools We'll Use
var gulp = require('gulp');
var $ = require('gulp-load-plugins')();
var del = require('del');
var runSequence = require('run-sequence');
var browserSync = require('browser-sync');
var pagespeed = require('psi');
var reload = browserSync.reload;
var exec = require('child_process').exec;
var notifier = require('node-notifier');
var bowerFiles = require('main-bower-files');

var isBuild = false;

var AUTOPREFIXER_BROWSERS = [
  'ie >= 10',
  'ie_mob >= 10',
  'ff >= 30',
  'chrome >= 34',
  'safari >= 7',
  'opera >= 23',
  'ios >= 7',
  'android >= 4.4',
  'bb >= 10'
];

function getRelativePath(absPath) {
    absPath = absPath.replace(/\\/g, '/');
    var curDir = __dirname.replace(/\\/g, '/');
    return absPath.replace(curDir, '');
}

function logUglifyError(error) {
    this.emit('end');
    var file = getRelativePath(error.fileName);
    $.util.log($.util.colors.bgRed('Uglify Error:'));
    $.util.log($.util.colors.bgMagenta('file: ') + $.util.colors.inverse(file));
    $.util.log($.util.colors.bgMagenta('line: '+error.lineNumber));
    //remove path from error message
    var message = error.message.substr(error.message.indexOf(' ')+1);
    $.util.log($.util.colors.bgRed(message));
    notifier.notify({ title: 'Gulp message', message: 'Uglify error!' });
}

function logCoffeeError(error) {
    this.emit('end');
    var file = getRelativePath(error.filename);
    $.util.log($.util.colors.bgRed('Coffee Error:'));
    $.util.log($.util.colors.bgMagenta('file: ') + $.util.colors.inverse(file));
    $.util.log($.util.colors.bgMagenta('line: '+error.location.first_line+', column: '+error.location.first_column));
    $.util.log($.util.colors.bgRed(error.name+': '+error.message));
    $.util.log($.util.colors.bgMagenta('near: ') + $.util.colors.inverse(error.code));
    notifier.notify({ title: 'Gulp message', message: 'Coffee error!' });
}

function logSASSError(error) {
    var file = getRelativePath(error.file);
    $.util.log($.util.colors.bgRed('Sass Error:'));
    $.util.log($.util.colors.bgMagenta('file: ') + $.util.colors.inverse(file));
    $.util.log($.util.colors.bgMagenta('line: '+error.line+', column: '+error.column));
    $.util.log($.util.colors.bgRed(error.message));
    notifier.notify({ title: 'Gulp message', message: 'SASS Error!' });
}

// Lint JavaScript
gulp.task('jshint', function () {
  return gulp.src('app/static/scripts/**/*.js')
    .pipe(reload({stream: true, once: true}))
    .pipe($.jshint())
    .pipe($.jshint.reporter('jshint-stylish'));
});

//Lint CoffeeScript
gulp.task('coffeelint', function() {
    return gulp.src('app/static/scripts/**/*.coffee')
      .pipe(reload({stream: true, once: true}))
      .pipe($.coffeelint())
      .pipe($.coffeelint.reporter());
});

// Optimize Images
gulp.task('images', function () {
  return gulp.src('app/static/images/**/*')
    /*.pipe($.cache($.imagemin({
      progressive: true,
      interlaced: true
    })))*/
    //Problems with caching.
    //We only use this task during building,
    //so caching is not very useful anyway.
    .pipe($.imagemin({
        progressive: true,
        interlaced: true
    }))
    .pipe(gulp.dest('dist/static/images'))
    .pipe($.size({title: 'images'}));
});


// Copy All Files At The Root Level (app)
gulp.task('copy', function () {
  return gulp.src([
    'app/**',
    '!app/**/__pycache__{,/**}',
    '!app/templates{,/**/*.html}',
    '!app/static{/images/**,/scripts/**,/styles/**}',
    '!app/static/bower_components{,/**/*}'

  ], {
    dot: true
  }).pipe(gulp.dest('dist'))
    .pipe($.size({title: 'copy'}));
});

// = true;

// Compile and Automatically Prefix Stylesheets
gulp.task('styles', function () {
  // For best performance, don't add Sass partials to `gulp.src`
  // If we edited a partial, we need to also edit a file that partial
  // is included at, otherwise $.changed() won't recognize the change.
    return gulp.src([
      'app/static/styles/*.scss',
      'app/static/styles/components/components.scss',
      'app/static/styles/materialize/sass/materialize.scss',
      'app/static/styles/**/*.css'
    ])
    .pipe($.sourcemaps.init())
    //.pipe($.changed('.tmp/styles', {extension: '.css'}))
    .pipe($.sass({
      precision: 10,
      onError: logSASSError
    }))
    //.pipe($.concat('main.css'))
    .pipe($.autoprefixer({browsers: AUTOPREFIXER_BROWSERS}))
    .pipe($.sourcemaps.write())
    .pipe(gulp.dest('.tmp/styles'))
    .pipe($.size({title: 'styles-dev'}))
    // Concatenate And Minify Styles for production
    .pipe($.if(isBuild, $.csso()))
        //.pipe($.uncss({
        //  html: [
        //    'app/templates/**/*.html'
        //  ],
        // CSS Selectors for UnCSS to ignore
        //  ignore: [
        //    /.navdrawer-container.open/,
        //    /.app-bar.open/
        //  ]
        //}))
    .pipe($.if(isBuild, $.concat('main.min.css')))
    //.pipe($.if(isBuild, $.rename({suffix: '.min'})))
    .pipe($.if(isBuild, gulp.dest('dist/static/styles')))
    .pipe($.if(isBuild, $.size({title: 'styles-dist'})));
});


//Concat and minify scripts
gulp.task('scripts', function() {
    return gulp.src([
          //'app/static/scripts/app.coffee',
          //'app/static/scripts/providers/**/*.{js,coffee}',
          //'app/static/scripts/controllers/**/*.{js,coffee}',
          'app/static/scripts/modules/**/*.{js,coffee}',
          'app/static/scripts/**/*.{js,coffee}'
    ])
    //.pipe($.changed('.tmp/scripts', {extension: '.js'}))
    .pipe($.sourcemaps.init())
    .pipe($.if('*.coffee', $.coffee({ bare: true })))
      .on('error',  logCoffeeError)
    .pipe($.concat('app-dev.js'))
    .pipe($.ngAnnotate())
    .pipe($.sourcemaps.write())
    .pipe(gulp.dest('.tmp/scripts'))
    .pipe($.size({title: 'scripts-dev'}))
    .pipe($.if(isBuild, $.uglify()))
      .on('error', logUglifyError)
    .pipe($.if(isBuild, $.rename('app.min.js')))
    .pipe($.if(isBuild, gulp.dest('dist/static/scripts')))
    .pipe($.if(isBuild, $.size({title: 'scripts-dist'})));
});

//Scan bower_components folder for main js and include them in base.html
gulp.task('bower-inject', function () {
  var target = gulp.src('app/templates/base.html');
  var sources = gulp.src(
    bowerFiles(),
    {read: false}
  );

  return target.pipe($.inject(sources, {
      ignorePath: 'app/static',
      transform: function(filepath, file, index, length, targetFile) {
        //remove first slash
        filepath = filepath.substring(1);
        var ext = filepath.split('.').pop();
        switch (ext) {
          case 'js':
            return '<script src="{% static "'+ filepath +'" %}"></script>';
          case 'css':
            return '<link rel="stylesheet" href="{% static "'+ filepath +'" %}">';
          default:
            return '<!--Unsupported file type: '+ filepath +' -->';
        }

      },
      name: 'bower'
    }))
    .pipe(gulp.dest('app/templates'));
});

gulp.task('bower-pack-css', function(){
  return gulp.src(bowerFiles({filter:'/**/*.css'}))
  .pipe($.concat('lib.min.css'))
  .pipe($.csso())
  .pipe(gulp.dest('dist/static/styles'))
  .pipe($.size({title: 'bower-pack-css'}));
});

gulp.task('bower-pack-js', function(){
  return gulp.src(bowerFiles({filter:'/**/*.js'}))
  .pipe($.concat('lib.min.js'))
  .pipe($.uglify())
  .pipe(gulp.dest('dist/static/scripts'))
  .pipe($.size({title: 'bower-pack-js'}));
});


// Scan Your HTML For Assets & Optimize Them
gulp.task('html', function () {
  //var assets = $.useref.assets({searchPath: '{.tmp,app/static}'});

  return gulp.src('app/templates/**/*.html')
    //.pipe(assets)
    // Concatenate And Minify JavaScript
    //.pipe($.if('*.js', $.uglify({preserveComments: 'some'})))
    // Remove Any Unused CSS
    // Note: If not using the Style Guide, you can delete it from
    // the next line to only include styles your project uses.
    //.pipe($.if('*.css', $.uncss({
    //  html: [
    //    'app/templates/**/*.html'
    //  ],
      // CSS Selectors for UnCSS to ignore
    //  ignore: [
    //    /.navdrawer-container.open/,
    //    /.app-bar.open/
    //  ]
    //})))
    // Concatenate And Minify Styles
    // In case you are still using useref build blocks
    //.pipe($.if('*.css', $.csso()))
    //.pipe(assets.restore())
    //.pipe($.useref())
    // Update Production Style Guide Paths
    //.pipe($.replace('components/components.css', 'components/main.min.css'))
    // Minify Any HTML
    .pipe($.htmlReplace({
      'css-lib': '<link rel="stylesheet" href="{% static "styles/lib.min.css" %}">',
      'js-lib': '<script src="{% static "scripts/lib.min.js" %}"></script>',
      'css-app': '<link rel="stylesheet" href="{% static "styles/main.min.css" %}">',
      'js-app': '<script src="{% static "scripts/app.min.js" %}"></script>'
    }))
    .pipe($.minifyHtml())
    // Output Files
    .pipe(gulp.dest('dist/templates'))
    .pipe($.size({title: 'html'}));
});

// Clean Output Directory
gulp.task('clean', del.bind(null, ['.tmp', 'dist/*', '!dist/.git'], {dot: true}));

//Activate virtualenv and run Django server
gulp.task('runserver', function() {
    var isWin = /^win/.test(process.platform);
     var cmd =  '. ../bin/activate';

    if (isWin) { //for Windows
        cmd = '..\\Scripts\\activate';
    }

    var proc = exec(cmd+' && python app/manage.py runserver');
});

gulp.task('runserver:dist', function() {
    var isWin = /^win/.test(process.platform);
     var cmd =  '. ../bin/activate';

    if (isWin) { //for Windows
        cmd = '..\\Scripts\\activate';
    }

    var proc = exec(cmd+' && python dist/manage.py runserver');
});


// Build and serve the output from the dist build
gulp.task('serve:dist', ['build', 'runserver:dist'], function () {
  browserSync({
    notify: false,
    proxy: '127.0.0.1:8000'
  });
});


// Build Production Files
gulp.task('build', ['clean'], function (cb) {
  isBuild = true;
  runSequence('styles', ['bower-inject', 'bower-pack-css', 'bower-pack-js', 'jshint', 'coffeelint', 'scripts',
    'html', 'images', 'copy'], cb);
});


// Watch Files For Changes & Reload, the default task
gulp.task('default', ['bower-inject', 'styles', 'jshint', 'coffeelint', 'scripts',
  'runserver'], function () {
  browserSync({
    notify: false,
    proxy: '127.0.0.1:8000'
  });

  gulp.watch(['app/**/*.html'], reload);
  gulp.watch(['app/static/styles/**/*.{scss,css}'], ['styles', reload]);
  gulp.watch(['app/static/scripts/**/*.js'], ['jshint']);
  gulp.watch(['app/static/scripts/**/*.coffee'], ['coffeelint']);
  gulp.watch(['app/static/scripts/**/*.{js,coffee}'], ['scripts', reload]);
  gulp.watch(['app/static/bower_components/**/*.{css,js}'], ['bower-inject', reload]);
  gulp.watch(['app/static/images/**/*'], reload);
});


// Run PageSpeed Insights
gulp.task('pagespeed', function (cb) {
  // Update the below URL to the public URL of your site
  pagespeed.output('example.com', {
    strategy: 'mobile',
    // By default we use the PageSpeed Insights free (no API key) tier.
    // Use a Google Developer API key if you have one: http://goo.gl/RkN0vE
    // key: 'YOUR_API_KEY'
  }, cb);
});

// Load custom tasks from the `tasks` directory
// try { require('require-dir')('tasks'); } catch (err) { console.error(err); }
