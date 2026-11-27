"""Tag handling for posts."""


def normalize_tags(raw):
    """Lowercase, strip and de-duplicate comma-separated tags, keeping the order they first appear."""
    cleaned = [tag.strip().lower() for tag in raw.split(",") if tag.strip()]
    return list(set(cleaned))


def tag_line(raw):
    """Tags as shown under a post: '#python #web'."""
    return " ".join(f"#{tag}" for tag in normalize_tags(raw))
