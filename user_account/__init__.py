default_app_config = "djolowin.user_account.apps.UserAccountConfig"


class CustomerEvents:
    """The different customer event types."""

    # Account related events
    ACCOUNT_CREATED = "account_created"
    ACCOUNT_ACTIVATED = "account_activated"
    ACCOUNT_DEACTIVATED = "account_deactivated"
    PASSWORD_RESET_LINK_SENT = "password_reset_link_sent"
    PASSWORD_RESET = "password_reset"
    PASSWORD_CHANGED = "password_changed"
    EMAIL_CHANGE_REQUEST = "email_changed_request"
    EMAIL_CHANGED = "email_changed"

    # Trade related events
    PLACED_SINGLE_ORDER = "placed_single_order"             # created a single item order
    PLACED_BUNDLE_ORDER = "placed_bundle_order"             # created a bundles items order
    CANCELLED_SINGLE_ORDER = "cancelled_single_order"       # cancelled a single item order
    CANCELLED_BUNDLE_ORDER = "cancelled_bundle_order"           # cancelled a bundle item order
    PLACED_AUCTION_BID = "placed_auction_bid"               # created an auction bid
    RECEIVED_AUCTION_BID = "received_auction_bid"           # received an auction bid
    CREATED_AUCTION = "created_auction"                     # created an auction
    DELETED_AUCTION = "deleted_auction"                     # deleted an auction
    DIGITAL_LINK_DOWNLOADED = "digital_link_downloaded"     # downloaded a digital good

    # Staff actions over customers events
    CUSTOMER_DELETED = "customer_deleted"  # staff user deleted a customer
    EMAIL_ASSIGNED = "email_assigned"  # the staff user assigned a email to the customer
    NAME_ASSIGNED = "name_assigned"  # the staff user added set a name to the customer
    NOTE_ADDED = "note_added"  # the staff user added a note to the customer

    CHOICES = [
        (ACCOUNT_CREATED, "The account was created"),
        (ACCOUNT_ACTIVATED, "The account was activated"),
        (ACCOUNT_DEACTIVATED, "The account was deactivated"),
        (PASSWORD_RESET_LINK_SENT, "Password reset link was sent to the customer"),
        (PASSWORD_RESET, "The account password was reset"),
        (
            EMAIL_CHANGE_REQUEST,
            "The user requested to change the account's email address.",
        ),
        (PASSWORD_CHANGED, "The account password was changed"),
        (EMAIL_CHANGED, "The account email address was changed"),
        (PLACED_SINGLE_ORDER, "A single order was placed"),
        (PLACED_BUNDLE_ORDER, "A bundled order was placed"),
        (CANCELLED_SINGLE_ORDER, "the single order was cancelled"),       
        (CANCELLED_BUNDLE_ORDER, "the bundle order was cancelled"), 
        (CREATED_AUCTION, "An auction was created"),
        (DELETED_AUCTION, "An auction was deleted"),                    
        (PLACED_AUCTION_BID, "An auction bid was submitted"),
        (RECEIVED_AUCTION_BID, "An auction bid was received"),
        (CUSTOMER_DELETED, "A customer was deleted"),
        (NAME_ASSIGNED, "A customer's name was edited"),
        (EMAIL_ASSIGNED, "A customer's email address was edited"),
        (NOTE_ADDED, "A note was added to the customer"),
    ]