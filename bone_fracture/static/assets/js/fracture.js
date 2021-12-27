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
            {'key': 'bone_1', 'value': 'Bone 1'},
            {'key': 'bone_2', 'value': 'Bone 2'},
            {'key': 'bone_3', 'value': 'Bone 3'},
            {'key': 'bone_4', 'value': 'Bone 4'}];

        var selectList = document.createElement("select");
        selectList.setAttribute("name", "select_input_" + counter);
        selectList.setAttribute("class", "form-select");
        div_6_1.appendChild(file);
        div6_2.appendChild(selectList);

        div.appendChild(div_6_1);
        div.appendChild(div6_2);

        for (var i = 0; i < bones.length; i++) {
            var option = document.createElement("option");
            option.value = bones[i].key;
            option.text = bones[i].value;
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
            processData: false,
            contentType: false,
        });
        request.done(function (response, textStatus, jqXHR) {
            $.unblockUI();
             // document.getElementById('ImageWithForm').style.display = "none";
            console.log("Hooray, it worked!");
        });
        request.fail(function (jqXHR, textStatus, errorThrown) {
            console.error("The following error occurred: ");
            $.unblockUI();
        });
    });

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