def test_search_by_doc_id(training_page):
    training_page.page.fill("input[placeholder*='search']", "65709")
    assert training_page.get_table_row_count() > 0