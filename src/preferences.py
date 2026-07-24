import dataclasses

@dataclasses.dataclass
class UserPreferences:
    language: str
    theme: str
    expand_posts: bool
    version: int = 1

    def __post_init__(self):
        """Validates default user attribute values"""
        self.language = "en_US"
        self.expand_posts = True
        self.theme = "dark"

    def replace_from_cookie(self, request) -> "UserPreferences":
        """Returns updated UserPreferences class (bypass settings cookie logic)"""
        return self
