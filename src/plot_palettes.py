"""Shared color palettes for the exploratory analysis notebook and related plots."""

from matplotlib.colors import LinearSegmentedColormap

CATEGORICAL_COLORS = ['#2B5C8F', '#4A9F82', '#7A8B99', '#DCA842']
SEQUENTIAL_COLORS = ['#EAF2F8', '#A9CCE3', '#5499C7', '#2471A3', '#154360']
DIVERGENT_COLORS = ['#C0392B', '#E5E7E9', '#2980B9']

SEQUENTIAL_CMAP = LinearSegmentedColormap.from_list('health_sequential', SEQUENTIAL_COLORS)
DIVERGENT_CMAP = LinearSegmentedColormap.from_list('health_divergent', DIVERGENT_COLORS)

PALETTES = {
    'categorical': CATEGORICAL_COLORS,
    'sequential': SEQUENTIAL_COLORS,
    'divergent': DIVERGENT_COLORS,
}

CMAPS = {
    'sequential': SEQUENTIAL_CMAP,
    'divergent': DIVERGENT_CMAP,
}


def get_palette(kind: str):
    """Return a palette list by kind."""

    return PALETTES[kind]


def get_cmap(kind: str):
    """Return a matplotlib colormap by kind."""

    return CMAPS[kind]
