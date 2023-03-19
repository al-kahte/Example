from app.exceptions import UserAlreadyExistsError
from app.models import User
from app.repositories import UserRepository
from app.services import UserService


def test_register_user():
    """
    Tests UserService.register_user() function.
    Registers a new user and checks that it is correctly added to the user repository.
    Also tests that a UserAlreadyExistsError is raised when trying to register an already existing user.
    """
    user_repository = UserRepository()
    user_service = UserService(user_repository)
    
    # Register new user
    user = user_service.register_user('alkahte', 'alkahte@outlook.com', 'password')
    
    # Check that user was registered correctly
    assert isinstance(user, User)
    assert user.username == 'alkahte'
    assert user.email == 'alkahte@outlook.com'
    assert user.password == 'password'
    assert user_repository.get_user('alkahte') == user

    # Check that trying to register an already existing user raises an exception
    try:
        user_service.register_user('alkahte', 'another@outlook.com', 'password')
        assert False, 'Expected exception to be raised'
    except UserAlreadyExistsError:
        pass


def test_authenticate_user():
    """
    Tests UserService.authenticate_user() function.
    Registers a new user and checks that authentication works as expected.
    """
    user_repository = UserRepository()
    user_service = UserService(user_repository)
    
    # Register new user
    user_service.register_user('alkahte', 'password')
    
    # Check that user can be authenticated with correct password
    user = user_service.authenticate_user('alkahte', 'password')
    assert isinstance(user, User)
    assert user.username == 'alkahte'
    assert user.password == 'password'

    # Check that user cannot be authenticated with incorrect password
    user = user_service.authenticate_user('algahte', '12345')
    assert user is None
