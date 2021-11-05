import pytest

from spaceUser.models import User


class TestSpaceUserModels:
    @pytest.mark.django_db
    def test_createUser(self):
        user = User.objects.create(
            last_name='jb', email='user@mail.com', password='password')
        assert str(user) == f"{user.last_name}"
