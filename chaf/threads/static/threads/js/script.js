$(function() {
	$("#order_by").change(function() {
		var href = window.location.href;
		href = href.replace(/page=\d+/, "page=1");
		href = href.replace(/order_by=[a-z_]+/, "");
		var order_by = $("#order_by").val();
		if (order_by == "year" || order_by == "alpha_sort") {
			href = href + "&order_by=" + order_by;
		}
		window.location.href = href;
	});
});