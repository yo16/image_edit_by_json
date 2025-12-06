from .change_size import apply_change_size
from .add_text import apply_add_text


EDIT_HANDLERS = {
    "change_size": apply_change_size,
    "add_text": apply_add_text,
}
