/* - gndrequest.js - */
/*
 * enables GND Triplestore requests for pndIdent within creator Input-fields 
 *
 *
 * Requires jQuery http://jquery.com/ 
 *
 */

         function pndFormCheck(number){
            var lastName = $('input.lastName');
            var firstName = $('input.firstName');
            if(lastName[number].value == null || lastName[number].value == "" || firstName[number].value == null || firstName[number].value == ""){
                alert('Füllen Sie bitte zunächst Nach- und Vornamenfelder aus');
            return false;
            }
            return true;

        }

	  function createUrl(number) {
            var lastName = $('input.lastName');
            var firstName = $('input.firstName');
            if(pndFormCheck(number)){
            PersonData = window.open("https://alkyoneus.hbz-nrw.de/gnd/gndrequest.jsp?firstName=" + firstName[number].value + "&lastName=" + lastName[number].value + "&index=" + number, "Person Data", "height=800,width=600,scrollbars=yes");
            //PersonData = window.open("https://alkyoneus.hbz-nrw.de/gnd/gndrequest.jsp?firstName=" + document.getElementById(('pndFirstName' + number)).value + "&lastName=" +  document.getElementById(('pndLastName' + number)).value + "&index=" + number, "Person Data", "height=800,width=600,scrollbars=yes");
	    //PersonData = window.open("file:///home/aquast/public_html/test_query.html?firstName=" + document.Autoren.fname.value + "&lastName=" + document.Autoren.lname.value, "Person Data", "height=300,width=600");
	    PersonData.focus();
            }
          return false;
	  }


	 function sendBackToParentWindow(gndData) {
	  var pkn = gndData;
          var url = window.location.search.split("=");
	  //window.opener.document.metadata_form.pndLastName0.value = pkn.children[1].children[0].children[0].textContent;
	  //window.opener.document.metadata_form.pndFirstName0.value = pkn.children[1].children[0].children[1].textContent;
          //window.opener.document.metadata_form.pndIdentNumber0.value = pkn.children[1].children[0].children[2].textContent;
          //alert("Insert: " + pkn.children[1].children[0].children[2].textContent);
	  window.opener.jQuery('input.lastName')[url[3]].value = pkn.children[1].children[0].children[0].textContent;
	  window.opener.jQuery('input.firstName')[url[3]].value = pkn.children[1].children[0].children[1].textContent;
	  window.opener.jQuery('input.PNDIdentNumber')[url[3]].value = pkn.children[1].children[0].children[2].textContent;
	  if(pkn.children[1].children[0].children[3]){
                window.opener.jQuery('input.academicTitle')[url[3]].value = pkn.children[1].children[0].children[3].textContent;
          }
          self.close();
	  return false;
	}


function addOnClicks() {
// function creates javascript submit buttons 
// for starting a GND triple store search in a new
// window 
var number = 0;
var pndField = $('input.PNDIdentNumber');
    
    pndField.parent()
         .append(function(index){return jQuery('<input type="image" src="searchpnd" alt="PND nach Person durchsuchen" onclick="createUrl(' + index + ');return false;" />');});
}

jQuery(document).ready(addOnClicks);
