if (!$) {
    $ = django.jQuery;
 }
function addSecs(d, s) {
    return new Date(d.valueOf() + s * 1000);
}
function doRun() {
    document.getElementById("msg").innerHTML = "Processing JS...";
    setTimeout(function() {
        start = new Date();
        end = addSecs(start, 5);
        do {
            start = new Date();
        } while (end - start > 0);
        document.getElementById("msg").innerHTML = "Finished Processing";
    }, 10);
 }
$(function() {
    $(".change_form_save").click(doRun);

    if (window.localStorage) {
        if (!localStorage.getItem("firstLoad")) {
            localStorage["firstLoad"] = true;
            window.location.reload();
        } else localStorage.removeItem("firstLoad");
    }
});