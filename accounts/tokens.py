from django.contrib.auth.tokens import PasswordResetTokenGenerator


class ConfirmEmailTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return str(user.pk) + user.password + str(user.is_active) + str(timestamp)

confirm_email_token_generator  = ConfirmEmailTokenGenerator()
