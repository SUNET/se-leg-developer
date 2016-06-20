'use strict';

if (!navigator.mediaDevices.getUserMedia) {
    var nonceInput = $('#nonce');
    var qrImageInput = $('#qrImage');

    // disable QR decoding modal
    nonceInput.attr('data-toggle', '');
    // trigger the image upload on click of the nonce input field
    nonceInput.click(function () {
        qrImageInput.click();
    });

    // set callback for the qrcode module
    qrcode.callback = function (data) {
        $('#nonce').val(data);
    };

    // trigger qr decode on image upload
    qrImageInput.change(function (event) {
        // Get a reference to the taken picture or chosen file
        var files = event.target.files;
        var file;
        if (files && files.length > 0) {
            file = files[0];
        }

        try {
            var imgURL = window.URL.createObjectURL(file);
            qrcode.decode(imgURL);
            URL.revokeObjectURL(imgURL);
        } catch (e) {
            console.log('Error: ' + e.message);
        }
    });
} else {
    var cameraStream;
    var qrCaptureInterval;
    var video = document.querySelector('video');
    var qrModal = $('#qrModal');

    // set callback for the qrcode module
    qrcode.callback = function (data) {
        $('#nonce').val(data);

        if (data.indexOf('error') === -1) {
            // stop capturing images from camera feed
            window.clearInterval(qrCaptureInterval);
            $('video').addClass('success-border');

            window.setTimeout(function () {
                qrModal.modal('hide');
                $('video').removeClass('success-border');
            }, 1000);
        }
    };

    // trigger continuous qr decode on video feed
    qrModal.on('shown.bs.modal', function () {
        Camera.start(function (stream) {
            cameraStream = stream;
            video.src = window.URL.createObjectURL(stream);
            video.onloadedmetadata = function () {
                qrCaptureInterval = window.setInterval(function () {
                    var canvas = document.createElement('canvas');
                    canvas.width = video.videoWidth;
                    canvas.height = video.videoHeight;
                    canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
                    qrcode.decode(canvas.toDataURL());
                }, 500);
            };
        });
    });

    // stop camera stream on modal close
    $('#qrModal').on('hide.bs.modal', function () {
        video.pause();
        video.src = '';
        if (cameraStream) {
            cameraStream.getVideoTracks()[0].stop();
        }
    });
}