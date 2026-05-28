"""Haiku generator using themed word banks."""

import random

THEMES = {
    "nature": {
        "5": ["the wind whispers soft", "autumn leaves are falling", "mountain fog descends", "river flows below"],
        "7": ["sunlight breaks through morning clouds", "petals drift across still water", "the old oak stands in silence"],
        "5_end": ["silence remains", "the earth breathes again", "stars begin to glow", "moonlight fills the lake"],
    },
    "city": {
        "5": ["neon lights flicker", "subway doors slide open", "rain on asphalt gleams", "traffic hums all night"],
        "7": ["strangers pass without a glance", "coffee cools on the counter", "the city never quite sleeps"],
        "5_end": ["horns fade away", "dawn breaks over rooftops", "pigeons take to flight", "windows catch the sun"],
    },
}


def generate_haiku(theme: str = "nature") -> str:
    """Return a random haiku string for the given theme."""
    if theme not in THEMES:
        raise ValueError(f"Unknown theme '{theme}'. Choose from: {', '.join(THEMES)}")

    bank = THEMES[theme]
    line1 = random.choice(bank["5"])
    line2 = random.choice(bank["7"])
    line3 = random.choice(bank["5_end"])
    return f"{line1}\n{line2}\n{line3}"


def list_themes() -> list[str]:
    """Return available theme names."""
    return list(THEMES.keys())


if __name__ == "__main__":
    import sys

    theme = sys.argv[1] if len(sys.argv) > 1 else "nature"
    print(generate_haiku(theme))
