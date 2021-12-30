window.addEventListener("load", function () {
    var counter = 0;
    document.getElementById("add_with").addEventListener("click", function () {
        var div = document.createElement("div");
        div.setAttribute("class", "row");
        counter += 1

        document.getElementById('upload_1').disabled = false;

        var div_6_1 = document.createElement("div");
        div_6_1.setAttribute("class", "col-md-6");
        var div6_2 = document.createElement("div");
        div6_2.setAttribute("class", "col-md-6");

        var file = document.createElement("input");
        file.setAttribute("type", "file");
        file.setAttribute("name", "file_input_" + counter);
        file.setAttribute("class", "form-control");
        file.setAttribute("accept", "image/*");
        var bones = [
            {'key': 'Elbow', 'value': 'XR_ELBOW'},
            {'key': 'Finger', 'value': 'XR_FINGER'},
            {'key': 'Forearm', 'value': 'XR_FOREARM'},
            {'key': 'Hand', 'value': 'XR_HAND'},
            {'key': 'Humerus', 'value': 'XR_HUMERUS'},
            {'key': 'Shoulder', 'value': 'XR_SHOULDER'},
            {'key': 'Wrist', 'value': 'XR_WRIST'}];

        var selectList = document.createElement("select");
        selectList.setAttribute("name", "select_input_" + counter);
        selectList.setAttribute("class", "form-select");
        div_6_1.appendChild(file);
        div6_2.appendChild(selectList);

        div.appendChild(div_6_1);
        div.appendChild(div6_2);

        for (var i = 0; i < bones.length; i++) {
            var option = document.createElement("option");
            option.value = bones[i].value;
            option.text = bones[i].key;
            selectList.appendChild(option);
        }
        document.getElementById("container1").appendChild(div);
    });
    var counter2 = 0
    document.getElementById("add_without").addEventListener("click", function () {
        // Create a div

        document.getElementById('upload_2').disabled = false;
        var div = document.createElement("div");
        counter2 += 1
        var file = document.createElement("input");
        file.setAttribute("type", "file");
        file.setAttribute("name", "file_input_" + counter2);
        file.setAttribute("accept", "image/*");
        div.appendChild(file);
        document.getElementById("container2").appendChild(div);
    });
    document.getElementById('upload_1').addEventListener("click", function () {
        $.blockUI({message: '<h1><img src="assets/img/busy.gif" /> Analyzing ;)</h1>'});
        var form = $('#ImageWithForm')[0];
        var formData = new FormData(form);
        var request = $.ajax({
            url: "http://localhost:5000/upload/with/type",
            type: "post",
            enctype: 'multipart/form-data',
            data: formData,
            // dataType: 'JSON',
            processData: false,
            contentType: false,
        });
        request.done(function (response, textStatus, jqXHR) {
            $.unblockUI();
            $("#results").html(createResultHTMLString(response.list_results));
             // document.getElementById('ImageWithForm').style.display = "none";
            console.log("Hooray, it worked!");
        });
        request.fail(function (jqXHR, textStatus, errorThrown) {
            console.error("The following error occurred: ");
            $.unblockUI();
        });
    });
    function createResultHTMLString(json_response)
    {
        var result_html = "<tr><th style=\"font-size: 1.5rem\">Image</th><th style=\"font-size: 1.5rem\">Classification</th></tr>";
        json_response.forEach(function(image){
            result_html += "<tr>"
            result_html += "<td>" +"<img src=\"" + image.image_path + "\" width=\"300\" height=\"300\">" + "</td>";
            result_html += "<td style=\"font-size: 1.5rem\">" + image.result + "</td>";
            result_html += "</tr>"
        })
        return result_html
    }
    document.getElementById('upload_2').addEventListener("click", function () {
        $.blockUI({message: '<h1><img src="assets/img/busy.gif" /> Analyzing ;)</h1>'});
        var form = $('#ImageWithoutForm')[0];
        var formData = new FormData(form);
        var request = $.ajax({
            url: "http://localhost:5000/upload/without/type",
            type: "post",
            enctype: 'multipart/form-data',
            data: formData,
            processData: false,
            contentType: false,
        });
        request.done(function (response, textStatus, jqXHR) {
            $.unblockUI();
            // document.getElementById('ImageWithoutForm').style.display = "none";
            console.log("Hooray, it worked!");
        });
        request.fail(function (jqXHR, textStatus, errorThrown) {
            console.error("The following error occurred: ");
            $.unblockUI();
        });

    });

});