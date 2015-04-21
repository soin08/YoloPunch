angular.module "Auth"
  .factory "User", ['$http', ($http) ->
      new class UserFactory
          constructor: ()->
            @loginUrl = '/accounts/login/.json'

          login: (username, password) ->
            credentials =
                username: username
                password: password

            console.log "logging in with credentials: username: #{credentials.username}, password: #{credentials.password}"
            $http.post @loginUrl, credentials
  ]
