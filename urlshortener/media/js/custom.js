$(document).ready(function() { 
    // call the tablesorter plugin 
    $("table.tablesorter").tablesorter({ 
        widthFixed: true, 
        container: $("#pager")
       
    }); 
});