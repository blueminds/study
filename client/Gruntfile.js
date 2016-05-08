module.exports = function(grunt) {
  // Do grunt-related things in here
  grunt.initConfig({
    stylus: {
            release: {
                files: { 'resources/global/global.css': ['resources/global/global.styl'],
                         'css/index.css': ['css/index.styl'],
                         'css/find.css': ['css/find.styl'],
                         'css/course_detail.css': ['css/course_detail.styl'],

                        },
                options: { compress: true, linenos: false },

            }
        },
    watch: {
        options: { livereload: true },
        styles: {
            files: ['resources/global/global.styl',
                    'css/index.styl',
                    'css/find.styl',
                    'css/course_detail.styl'
            ],
            tasks: ['stylus']
        },
        html: {
            files: ['index.html'] // no tasks, just live reload
        }
    },
    connect: {
      server: {
        options: {
          port: 8000,
          base: './',
          keepalive:true
        }
      },
    }
  });


  grunt.loadNpmTasks('grunt-contrib-connect');
  grunt.loadNpmTasks('grunt-contrib-stylus');
  grunt.loadNpmTasks('grunt-contrib-watch');

  grunt.registerTask("tarea", function(){
    console.log("ejecutando una tarea");
  });


};
