#LoginController
class LoginController
  constructor: (@$scope, @$window, @User) ->

  login: =>
    th = @
    th.$scope.loginForm.processing = true
    @User.login(@$scope.username, @$scope.password)
      .success (data, status) ->
        th.$scope.loginForm.processing = false
        th.$scope.loginForm.loginFailed = false
        console.log status
        th.$window.location = '/'
      .error (data, status) ->
        th.$scope.loginForm.processing = false
        th.$scope.loginForm.loginFailed = true
        console.log data

angular.module 'Auth'
.controller 'LoginController', ['$scope', '$window', 'User', LoginController]
