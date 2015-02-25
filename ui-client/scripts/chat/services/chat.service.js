/**
 * Created by mayureshp on 2/17/2015.
 */

angular.module("chat").
    factory("ChatService", ["$firebase", function($firebase) {
        console.log("In service");
        var firebaseUrl = "https://dazzling-fire-5952.firebaseio.com/PythonChatDemo/Track";
        var chatRef = new Firebase(firebaseUrl);

        chatRef.on("child_added", function(snapshot) {
            var chat_message = snapshot.val();
            console.log("Chat message = " + chat_message);
        })

    }]);