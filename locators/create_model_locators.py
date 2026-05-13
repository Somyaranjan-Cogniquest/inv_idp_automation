# Page identity
CREATE_MODEL_TITLE = "text=Create Model"
CREATE_MODEL_FORM = "form"

# Buttons
NEXT_BUTTON = "button:has-text('Next')"
CREATE_BUTTON = "button:has-text('Create Model')"
CANCEL_BUTTON = "button:has-text('Cancel')"

# Breadcrumb
BREADCRUMB_HOME = "nav[aria-label='breadcrumb'] >> text=Home"

# Inputs (best practice: locate by label text)
MODEL_NAME_INPUT = "input[placeholder*='Model Name'], input[name*='model'], input[id*='model']"

# Validation messages
ERROR_MESSAGE = ".error-msg, .Mui-error, text=/required/i, text=/invalid/i"

# Example mandatory fields (replace with actual once you inspect)
PROJECT_DROPDOWN = "text=Project >> xpath=.."
MODEL_TYPE_DROPDOWN = "text=Model Type >> xpath=.."