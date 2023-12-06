# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.user_model import UserModel  # noqa
from app.models.token_model import Token  # noqa
from app.models.message_model import MessageModel