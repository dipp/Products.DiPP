/*
 * make the lengthy metadata form easier to fill out, without server communication
 *   
 * $Id$
 */

function get_next_ids(current_id) {
    var sep = '_'
    var parts = current_id.split(sep);
    var number = parseInt(parts[1], 10) + 1;
    return [number, parts[0] + sep + number];
}


function add_field () {
    var metadata_field = $('#creatorPerson');
    var button = $('input.addfield', metadata_field);
    //$("form").submit(function (event) {
    button.click(function (event) {
        event.preventDefault();
        var tabelle = $('table', metadata_field);
        var last_row = $('tr:last', tabelle);
        var last_id = last_row.attr('id');
        var next_ids = get_next_ids(last_id);
        console.log(next_ids);
        var new_row = $('tr:last', tabelle).clone().appendTo(tabelle);
        $('input', new_row).attr('value','');
        $('.counter', new_row).attr('value',next_ids[0]);

        if (new_row.hasClass('odd')) {
            new_row.removeClass('odd');
            new_row.addClass('even');
        } else {
            new_row.removeClass('even');
            new_row.addClass('odd');
        };
        new_row.attr('id', next_ids[1])
        
        
        return false;
    })
}


(function($) {
	$(document).ready(add_field);
})(jQuery);
