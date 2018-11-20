

@implementer(IIdentityPolicy)
class CompatibilityIdentityPolicy(object):
    """ An identity policy that operates as a passthru for the legacy
    :class:`AuthenticationPolicy`
    """
    def __init__(self, policy):
        self._policy = policy

    def identify(self, request):
        return self._policy(self).authenticated_userid(request)
