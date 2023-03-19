from behave import given, when, then
from app.models import User
from app.repositories import UserRepository
from app.services import UserService


@given("the following user is not registered")
def given_user_is_not_registered(context):
    """
    Given a table of user data, creates an instance of an UserRepository and adds the users to it.
    Stores the repository in the context object for later use.
    """
    user_table = context.table
    user_repository = UserRepository()
    for user_row in user_table:
        user = User(user_row["username"], user_row["email"], user_row["password"])
        user_repository.add_user(user)
    context.user_repository = user_repository


@when("the user registers with the following information")
def when_user_registers_with_info(context):
    """
    Given a table of user data, creates an instance of a UserService with the previously stored user_repository.
    Registers the user with the provided data and stores the resulting User object in the context object for later use.
    """
    user_table = context.table
    user_service = UserService(context.user_repository)
    for user_row in user_table:
        user = user_service.register_user(
            user_row["username"], user_row["email"], user_row["password"]
        )
        context.user = user


@then("the user is registered successfully")
def then_user_should_see_registration_success(context):
    """
    Asserts that a User object has been stored in the context object after registration.
    """
    assert context.user is not None


@then("the user can authenticate with the following information")
def then_user_can_authenticate_with_info(context):
    """
    Given a table of user data, creates an instance of a UserService with the previously stored user_repository.
    Attempts to authenticate the user with the provided data and asserts that a User object is returned.
    """
    user_table = context.table
    user_service = UserService(context.user_repository)
    for user_row in user_table:
        user = user_service.authenticate_user(
            user_row["username"], user_row["password"]
        )
        assert user is not None
