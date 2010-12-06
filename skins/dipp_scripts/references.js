/*
 * Display the full references of a DocBook converted article
 * as tooltips of the reference to the footnote
 * Requires jQuery http://jquery.com/ and jQuery Tools Tooltip
 * http://flowplayer.org/tools/tooltip/index.html   
 *   
 * $Id$
 */


/* return an assocated array with the ID of the reference as key and 
 * the full reference as value
 */
function getReferences() {
	var references = [];
	var content = $("#region-content");  
	var footnotes = $("div.footnotes div.footnote", content);
	for (var i = 0; i < footnotes.length; i++ ){
		var ref_id = $("span.footnoteReference a", footnotes[i]).attr('id');
		var ref_content = $("p", footnotes[i]).html();
		references[ref_id] = ref_content;
		}
	return references;
	}


/*
 * scan the article for footnote references and put a div containing
 * the full reference after the hyperlink. This div is used as tooltip 
 */
function inlineFootnotes() {
	var ftn = "ftn.";   // ID prefix of the references in the footnotes
	var refs = getReferences();
	var content = $("#region-content");
	var footnoteReferences = $("span.footnoteReference",content);
	for (var i = 0; i < footnoteReferences.length; i++ ){
		var link = $("a", footnoteReferences[i]);
		var ref_id = link.attr('id');
		if (ref_id.substring(0,4) != ftn) {
			var id = ftn + ref_id;
			link.after('<div class="inlineReference"></div>');
			var tt = $("div",footnoteReferences[i]);
			tt.html(refs[id]);
			$("span",tt).remove(".footnoteReference");
			link.tooltip({
				//effect: 'fade',
				//fadeOutSpeed: 50,
				//predelay: 400,
				delay: 500,
				position: "bottom right",
				offset: [-50, -80]
			});
		}
	}
}

$(document).ready(inlineFootnotes);
