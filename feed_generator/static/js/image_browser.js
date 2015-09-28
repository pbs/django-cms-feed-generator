// Holds the current image field name
var image_field_id= '';
var filer_image_url = '';

function id_to_windowname(text) {
    text = text.replace(/\./g, '__dot__');
    text = text.replace(/\-/g, '__dash__');
    return text;
}

function showRSSImageLookupPopup(triggeringLink, field_id, filer_url) {
    image_field_id = field_id;
    filer_image_url = filer_url;
    var name = triggeringLink.id.replace(/^lookup_/, '');
    name = id_to_windowname(name);
    var href;
    if (triggeringLink.href.search(/\?/) >= 0) {
    	href = triggeringLink.href + '&pop=1';
    } else {
	    href = triggeringLink.href + '?pop=1';
    }
    var win = window.open(href, name, 'height=500,width=800,resizable=yes,scrollbars=yes');
    win.focus();
    return false;
}

dismissRelatedImageLookupPopup = function(win, chosenId, chosenThumbnailUrl, chosenDescriptionTxt) {
    win.close();
    var jxhr = jQuery.ajax({
                url: filer_image_url,
                data: {'id': chosenId},
                success: function(data){
                    if (data.url){
			jQuery("span.browse_image_invalid").html('');
                        jQuery('#'+image_field_id).val(data.url);
                    }
                    else{
			jQuery("span.browse_image_invalid").attr("style","color:red;font-weight:bold;");
                        jQuery("span.browse_image_invalid").html('Please select a valid image type.');
                    }
                },
                error: function(data){
                    alert('Error retrieving file information.');
                }
            });
        return jxhr;
};
