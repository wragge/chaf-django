$(function() {
	$("#browse").click(function() {
		var year = $("#year").val();
		window.location.href = "/tungwah/issues/" + year;
	});
	$("#order_by").change(function() {
		var href = window.location.href;
		href = href.replace(/page=\d+/, "page=1");
		href = href.replace(/order_by=[a-z_]+/, "");
		var order_by = $("#order_by").val();
		if (order_by == "issue_date") {
			href = href + "&order_by=" + order_by;
		}
		window.location.href = href;
	});
});