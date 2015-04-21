#RegisterController
class RegisterController
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
.controller 'RegisterController', ['$scope', '$window', 'User', RegisterController]
