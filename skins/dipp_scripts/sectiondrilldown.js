/*
 * drilldown for the recent_articles_by_section template
 * allws the submissions of the drilldown form without 
 * pressing the submit button. THe button is hidden, when
 * javascript is enabled
 *   
 * $Id: references.js 3106 2011-04-27 20:19:40Z reimer $
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
