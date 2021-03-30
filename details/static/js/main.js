const endpoint = ''
const delay_by_in_ms = 100
let scheduled_function = false

let ajax_call = function (endpoint, request_parameters) {
    $.getJSON(endpoint, request_parameters)
        .done(response => {
            // replace the HTML contents
            $('div.replace').html(response['search_result'])
        })
}


function keyp(val) {
    const request_parameters = {
        q: val 
    }
    // if scheduled_function is NOT false, cancel the execution of the function
    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }
    // setTimeout returns the ID of the function to be executed
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
}