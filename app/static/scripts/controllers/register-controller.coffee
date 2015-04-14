#Register Controller
class RegisterController
  constructor:($scope, @User) ->
    @user =
      username:''
      password: ''
      first_name: ''
      last_name: ''
    $scope.userType = 'guest'

  register: ->
    alert "register"
    #@User.create(@user)

angular.module 'Auth'
  .controller 'RegisterController', ['$scope','User', RegisterController]
