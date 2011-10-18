/*
 * make the lengthy metadata form easier to fill out, without server communication
 *   
 * $Id$
 */


function add_field () {
    var metadata_field = $('#creatorPerson');
    var button = $('input.addfield', metadata_field);
    var tabelle = $('table', metadata_field);
    var last_row = $('tr', tabelle);
    button.click(function() {
        alert(last_row);
        return false;
    })
}

(function($) {
	$(document).ready(add_field);
})(jQuery);
