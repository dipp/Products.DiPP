$(document).ready(inlineFootnotes);

function inlineFootnotes() {
	var ftn = "ftn."
	var refs = getReferences();
	var ids = Array()
	var content = $("#region-content");
	var footnoteReferences = $("span.footnoteReference",content);
	for (var i = 0; i < footnoteReferences.length; i++ ){
		var link = $("a", footnoteReferences[i])  
		ref_id = link.attr('id');
		if (ref_id.substring(0,4) != ftn) {
			id = ftn + ref_id;
			link.after('<div class="inlineReference"></div>');
			var tt = $("div",footnoteReferences[i])
			tt.html(refs[id]);
			$("span",tt).remove(".footnoteReference");
			link.tooltip({
						//effect: 'fade',
						//fadeOutSpeed: 50,
						//predelay: 400,
						delay: 500,
						position: "bottom right",
						offset: [-50, -80]
					}		
			
			);
		}
	}
	//alert(refs[ids[2]]);
}

function getReferences() {
	var references = Array();
	var content = $("#region-content");  
	var footnotes = $("div.footnotes div.footnote", content);
	for (var i = 0; i < footnotes.length; i++ ){
		ref_id = $("span.footnoteReference a", footnotes[i]).attr('id');
		ref_content = $("p", footnotes[i]).html();
		references[ref_id] = ref_content;
		};
	//alert(references['ftn.d53e195']);
	return references
	};

	