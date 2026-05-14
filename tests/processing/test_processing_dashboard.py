def test_processing_dashboard_basic_validations(processing_dashboard_page):

    assert processing_dashboard_page.is_processing_dashboard_loaded(), \
        "Processing Dashboard breadcrumb not visible"

    assert processing_dashboard_page.is_documents_sidebar_selected(), \
        "Documents sidebar not highlighted"

    # Charts
    assert processing_dashboard_page.are_charts_visible(), \
        "Processing charts not visible"

    # Table
    assert processing_dashboard_page.is_table_visible(), \
        "Documents table not visible"

    row_count = processing_dashboard_page.get_table_row_count()
    assert row_count > 0, "No documents found in table"

    # Pagination
    assert processing_dashboard_page.is_pagination_visible(), \
        "Pagination not visible"
    
    