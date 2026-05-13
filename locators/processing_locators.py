# locators/processing_locators.py

# Breadcrumb container (we'll check text inside it)
BREADCRUMB_CONTAINER = "nav[aria-label='breadcrumb']"

# Sidebar
SIDEBAR_DOCUMENTS = "li[title='Documents']"

# Review Status
REVIEW_APPROVED = "input[type='radio'][value='approved']"
REVIEW_NOT_APPROVED = "input[type='radio'][value='not approved']"
REVIEW_REJECTED = "input[type='radio'][value='rejected']"
REVIEW_DELETED = "input[type='radio'][value='deleted']"

# Doc Status
DOC_PROCESSED = "input[type='radio'][value='processed']"
DOC_UNPROCESSED = "input[type='radio'][value='unprocessed']"

# Color
COLOR_GREEN = "input[type='radio'][value='green']"
COLOR_RED = "input[type='radio'][value='red']"

CLEAR_FILTERS_BTN = "button:has-text('Clear Filters')"

# Table
TABLE = "table.dashboard-table"
TABLE_ROWS = "tbody tr.tablerow"
DOC_NAME_CELL = "td.DatarowColor"

# Pagination
PAGINATION = "div.pagination"