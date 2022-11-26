from django.contrib.auth.models import User
from django.test import TestCase
from profiles.models import UserProfile

"""
class to test model Profile
"""


class ProfileTestCase(TestCase):

    def setUp(self):
        """
        Defined function before condition for test
        """

        self.user = User.objects.create(username='test33', password='test33')
        self.user.save()

        profile = UserProfile.objects.create(
            user=self.user,
            default_phone_number='0834187086',
            default_street_address1='grafton street',
            default_town_or_city='Dublin',
            default_county='ireland',
            default_postcode='32653'
        )

#    def test_profile_return_str(self):
#        """
#        Test string for UserProfile
#        """
#        profile = UserProfile.objects.get(user=self.user)
#        self.assertEquals(profile.__str__(), self.user.username)
