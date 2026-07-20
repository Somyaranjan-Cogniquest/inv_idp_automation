def test_training_dashboard(training_page):

    assert training_page.is_documents_table_visible()
    assert training_page.are_charts_visible()

    training_page.extract_chart_data()

    docs = training_page.get_documents_count()
    print(f"\nDocuments Count: {docs}")
    assert docs > 0