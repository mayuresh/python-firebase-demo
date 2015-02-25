/**
 * Created by mayureshp on 2/17/2015.
 */

angular.module("chat").
    controller("ChatController", ['$scope', '$firebase', function ($scope, $firebase) {
        console.log("In controller");
        var firebaseUrl = "https://dazzling-fire-5952.firebaseio.com/PythonChatDemo/Messages";
        var chatRef = new Firebase(firebaseUrl);
        var sync = $firebase(chatRef);

        $scope.username = "New User";
        $scope.chat_messages = sync.$asArray();

        $scope.newMessageKeyPress = function(keyEvent) {
            if (keyEvent.which === 13) {
                console.log("Enter clicked : " + $scope.new_message);
                $scope.chat_messages.$add({name: $scope.username, message: $scope.new_message, $priority: Date.now()});
                $scope.new_message = "";
            }
        }
    }]);
