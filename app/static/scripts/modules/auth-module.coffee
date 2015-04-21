#Authentication module
angular.module 'Auth', ['ngCookies','ngAnimate', 'ui.materialize']
  .config ['$httpProvider', ($httpProvider) ->
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  ]
console.log "aut module loaded heh"
