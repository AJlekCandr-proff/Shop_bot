from aiogram import Router

from .handler_catalog import router as router_catalog
from .handler_support import router as router_support
from .handler_rules import router as router_rules
from .user_transaction import router as router_transactions
from .user_profile import router as router_person_profile
from .cmd_start import router as router_cmd_start


router = Router(name=__name__)


router.include_routers(
    router_catalog,
    router_transactions,
    router_person_profile,
    router_cmd_start,
    router_support,
    router_rules,
)
