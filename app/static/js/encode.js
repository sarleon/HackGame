/**
 * Created by root on 17-3-9.
 */
function base64_encode(input) {
    return window.btoa(input);
}

function base64_decode(input) {
    return window.atob(input);
}

function url_encode(input) {
    return encodeURI(input);
}

function url_decode(input) {
    return decodeURI(input);

}
function html_encode(input) {
    return input;

}

function html_decode(input) {
    return input;

}

    


function ascii_to_string(input) {
     return input;
}

function string_to_ascii(input) {
        return input;
}
