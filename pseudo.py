
# This file will get edited down the line, but stores my notes on what exactly is being done.

# - Main Page
#   - Will probably get renamed to "Options"
# - Notes
# - Agitha's Castle
# - Jovani's Poes
#   x Rename to "Redemption"

# Main Page ===================================================================
# - Pick Spoiler Log
#   x May get made into its own tab.
#     x Ensures that .jsons are provided.
#       x If none is provided, it tells you to put a spoiler log in the folder
#         it is looking for them in
#       x If one or more is provided, creates a dropdown for you to select from,
#         and a confirmation button.
#         \ Loading a spoiler log resets the tracker, then autofills the Agitha
#           and Jovani tabs.
# x Reset Tracker
#   x Clears the notepad, and sets the Agitha's and Jovani's tabs to notepads.
#     x If they do not exist, recreate them (though this is a bug that is
#       currently in the app)
# x Race Mode
#   x Deletes the Agitha and Jovani Tabs, and resets the notepad to empty
# =============================================================================

# Notes =======================================================================
# x A blank notepad for the user to jot down notes. Nothing fancy.
# =============================================================================

# Agitha's Castle =============================================================
# x By default, a notepad for user to jot down notes, nothing fancy.
# - If she has items, then autofill with a checklist.
#   - Update the text to say "Agitha gives you GREAT HAPPINESS:"
#     - I would like to in the future update the text to be more accurate
#   - List the items that she has a checklist
#     - Once all the items are selected, update the text to say
#       "Congratulations! There is nothing left to collect here.\nYou have
#       collected the following items from Agitha's Castle:"
#       - In the future, I want to just say "Agitha" instead of the full name.
# - If she has no items, then close the tab
#   - I would like this to somehow otherwise indicate that Agitha is not a
#     valuable set of checks, than just closing the tab. But for now, closing
#     the tab works.
# =============================================================================

# Jovani's Redemption =========================================================
# x By default, a notepad for the user to jot down notes, nothing fancy.
# - If a sign is provided, autofill with a checklist.
#   - Disable checks which are said to be bad rewards
#     - If all checks are bad, then his sign says "Jovani remains greedy, and
#       does not pay you well."
#   - If he has any good, his sign text says "Jovani has learned, and rewards
#     you with the following:"
#   - Once all items are collected, if there are any good, update the text to
#     say "Congratulations! There is nothing left to collect here.\nYou have
#     collected the following items from Jovani's Redemption:"
#     - I want to in the future just say "Jovani" instead of the full name.
# =============================================================================
