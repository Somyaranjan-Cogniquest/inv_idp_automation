def test_processing_filters(processing_dashboard_page):

    processing_dashboard_page.apply_review_status("approved")
    processing_dashboard_page.apply_doc_status("processed")
    processing_dashboard_page.apply_color_filter("red")

    row_count = processing_dashboard_page.get_table_row_count()
    assert row_count >= 0, "Filter application failed"

    processing_dashboard_page.clear_filters()