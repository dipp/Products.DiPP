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


function add_field(meta_id) {
    var metadata_field = $(meta_id);
    var button = $('input.addfield', metadata_field);
    button.click(function (event) {
        event.preventDefault();
        var tabelle = $('table tbody', metadata_field);
        var last_row = $('tr:last', tabelle);
        var last_id = last_row.attr('id');
        var next_ids = get_next_ids(last_id);
        console.log(next_ids);
        var new_row = $('tr:last', tabelle).clone().appendTo(tabelle);
        $('input', new_row).val('');
        $('textarea', new_row).val('');
        $('option', new_row).removeAttr('selected');
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
    });
};

function remove_field(meta_id) {
    var metadata_field = $(meta_id);
    var button = $('input.removefield', metadata_field);
    button.click(function (event) {
        event.preventDefault();
        var tabelle = $('table >tbody', metadata_field);
        var rowCount = $('table >tbody >tr', metadata_field).length;            
        var searchIDs = $("input.counter:checkbox:checked", tabelle).map(function(){
          return $(this).val();
        }).get();

        for (var i=0; i < searchIDs.length; i++){
            var row_id = meta_id + "_" + searchIDs[i];
            var tr = $(row_id, tabelle);
            if (rowCount > 1){
                tr.remove();
                rowCount--;
            } else {
                $('input', tr).attr('value','');
            };
        };
    });
};

(function($) {
	$(document).ready(function(){
        var meta_ids = [
            "#creatorPerson",
            "#abstract",
            "#title"
        ]
        for (var i=0, len=meta_ids.length; i<len; i++){
            add_field(meta_ids[i]);
            remove_field(meta_ids[i]);
        }
    });
})(jQuery);
