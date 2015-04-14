class UserFactory
  constructor: ->
    @userListUrl = 'api/v1/users/'

  create: (user) ->
    $http.post @userListUrl, user

angular.module "Auth"
  .factory "User", -> new UserFactory()
