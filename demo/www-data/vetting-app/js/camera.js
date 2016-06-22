var Camera = (function () {
    var moduleObject = {};

    moduleObject.start = function (callback) {
        var constraints = {video: {facingMode: 'environment'}};
        var cameraFeedPromise = navigator.mediaDevices.getUserMedia(constraints);
        cameraFeedPromise.then(function (mediaStream) {
            callback(mediaStream);
        });
        cameraFeedPromise.catch(function (err) {
            console.log(err.name);
        });
    };
    return moduleObject;
})();
