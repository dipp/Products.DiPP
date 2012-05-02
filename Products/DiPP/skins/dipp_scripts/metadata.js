/*
 * make the lengthy metadata form easier to fill out, without server communication
 *   
 * $Id$
 */


function add_field () {
    var metadata_field = $('#creatorPerson');
    var button = $('input.addfield', metadata_field);
    var tabelle = $('table', metadata_field);
    var last_row = $('tr:last', tabelle);
    //$('input', empty_row).attr('value','');
    button.click(function() {
        last_row.after("<tr class='new'>" + last_row.html() + "</tr>");
        var new_row = $('table tr:last', metadata_field);
        $('input', new_row).attr('value','');
        return false;
    })
}

(function($) {
	$(document).ready(add_field);
})(jQuery);
