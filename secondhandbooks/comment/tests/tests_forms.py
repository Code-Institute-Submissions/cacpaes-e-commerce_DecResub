from django.test import TestCase
from comment.forms import CommentForm


"""
class to test form CommentForm
"""
class CommentFormTestCase(TestCase):

    def test_comment_form_valid(self):
        """
        Check if the form is valid
        """
        form = CommentForm(data={
            'name': 'Teste',
            'email': 'teste@gmail.com',
            'body': 'This is a valid'
        })
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid_skip_name(self):
        """
        Check if the form is invalid, parameter name not invite
        """
        form = CommentForm(data={
            'email': 'colombiano@gmail.com',
            'body': 'This is a valid'
        })
        self.assertFalse(form.is_valid(), form.errors)

    def test_comment_form_invalid_skip_email(self):
        """
        Check if the form is invalid, parameter email not invite
        """
        form = CommentForm(data={
            'name': 'Colombiano',
            'body': 'This is a valid'
        })
        self.assertFalse(form.is_valid(), form.errors)


    def test_comment_form_invalid_skip_body(self):
        """
        Check if the form is invalid, parameter body not invite
        """
        form = CommentForm(data={
            'email': 'colombiano@gmail.com',
            'name': 'Colombiano'
        })
        self.assertFalse(form.is_valid(), form.errors)