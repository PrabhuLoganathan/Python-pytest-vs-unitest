import pytest

pytestmark = pytest.mark.usefixtures('db_session')


def test_db_access_save():
    """Test db save"""
    print('######## running save')


def test_db_access_delete():
    """Test db deletion"""
    print('######## running delete')

@pytest.mark.non_db
def test_non_db_action():
    """Test does not depend on DB"""
    print('######## running non db')
