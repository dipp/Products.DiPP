/*
 * make the lengthy metadata form easier to fille out, without server communication
 *   
 * $Id: sectiondrilldown.js 3157 2011-05-23 19:38:42Z reimer $
 */

function add_row() {
    alert("neue reihe");
    return false;
}

function add_field () {
    var metadata_field = $('#creatorPerson');
    var button = $('input.addfield', metadata_field);
    var tabelle = $('table', metadata_field);
    button.click(add_row)
}

(function($) {
	$(document).ready(add_field);
})(jQuery);
