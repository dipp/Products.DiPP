/*
 * drilldown for the recent_articles_by_section template
 * allows the submissions of the drilldown form without 
 * pressing the submit button. The button is hidden, when
 * javascript is enabled
 *   
 * $Id$
 */



function drillDown() {
    var drilldownform = $("#sections-drill-down");
    var button = $('input[type=submit]', drilldownform);
    button.remove();
    var boxes = $('input[type=checkbox]', drilldownform);
    boxes.change(function() {
        $(this).closest("form").submit();
    });
}
(function($) {
	$(document).ready(drillDown);
})(jQuery);
