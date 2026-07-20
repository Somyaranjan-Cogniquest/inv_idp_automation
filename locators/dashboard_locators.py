MODEL_NAME_CELL = "td.Datarow12v5"

# Breadcrumb
BREADCRUMB_CONTAINER = "nav[aria-label='breadcrumb']"
BREADCRUMB_MODEL = "nav[aria-label='breadcrumb'] li a:not(:has-text('Home'))"

# Heading
MODEL_NAME_HEADING = "h2"

# Cards
CONFIGURE_MODEL_CARD = "div:has(svg[data-testid='SettingsIcon'])"
TRAINING_CARD = "div:has(svg[data-testid='ModelTrainingIcon'])"
PROCESSING_DASHBOARD_CARD = "div:has(svg[data-testid='DatasetIcon'])"
DOCUMENT_ANALYTICS_CARD = "div:has(svg[data-testid='AnalyticsIcon'])"

# Header / Navigation
COGNIQUEST_LOGO = "img[src*='congiquest-logo']"
BREADCRUMB_HOME = "nav[aria-label='breadcrumb'] li a"
SIDEBAR_HOME_ICON = "li[title='Home']"

# Table Header
MODEL_TABLE_HEADER = "tr:has(th:has-text('Model Name'))"
MODEL_NAME_HEADER = "th:has-text('Model Name')"
MODEL_ID_HEADER = "th:has-text('Model ID')"
MODEL_TABLE_HEADER_ROW = "tr:has(th:has-text('Model Name'))"


# Table Rows
TABLE_ROWS = "tr:has(td.Datarow12v5)"
MODEL_NAME_CELL = "td.Datarow12v5"
MODEL_ID_CELL = "td.Datarow122v5"
CREATE_MODEL_BUTTON = "button:has-text('Create Model')"

# Status Icons
TRAINED_STATUS_ICON = "svg[title='Trained']"
NOT_TRAINED_STATUS_ICON = "svg[title='Not Trained']"

# Action Menu
ACTION_MENU_BUTTON = "img[src*='menu-horizontal']"
# action menu icon appears per row (many), so always use first row in page methods
ACTION_MENU_ICON = "img[src*='menu-horizontal']"

# sorting headers (click by text)
HEADER_BY_TEXT = "th:has-text('{col}')"

MODEL_TABLE_HEADER = "tr:has(th:has-text('Model Name'))"
MODEL_NAME_CELL = "td.Datarow12v5"
TABLE_ROWS = "tr:has(td.Datarow12v5)"

BREADCRUMB_CONTAINER = "nav[aria-label='breadcrumb']"