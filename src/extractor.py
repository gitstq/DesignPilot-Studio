#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Design Token Extractor - Extract design tokens from CSS/HTML files
设计令牌提取器

Supports extraction from:
- CSS files: colors, spacing, typography, shadows, border-radius
- HTML files: inline styles, class-based analysis
"""

import re
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from urllib.request import urlopen
from urllib.error import URLError


class DesignExtractor:
    """Extract design tokens from CSS/HTML source files."""

    # Regex patterns for CSS extraction
    COLOR_PATTERNS = [
        r'#[0-9a-fA-F]{3,8}\b',
        r'rgba?\([^)]+\)',
        r'hsla?\([^)]+\)',
    ]

    SPACING_VALUES = [
        '0', '1px', '2px', '4px', '5px', '8px', '10px', '12px', '14px', '15px',
        '16px', '18px', '20px', '24px', '28px', '30px', '32px', '36px', '40px',
        '48px', '56px', '64px', '72px', '80px', '96px', '112px', '128px',
        '0.25rem', '0.5rem', '0.75rem', '1rem', '1.25rem', '1.5rem', '2rem',
        '2.5rem', '3rem', '4rem', '5rem', '6rem', '8rem',
    ]

    FONT_WEIGHTS = ['100', '200', '300', '400', '500', '600', '700', '800', '900']
    FONT_SIZES = [
        '10px', '11px', '12px', '13px', '14px', '15px', '16px', '17px', '18px',
        '20px', '22px', '24px', '26px', '28px', '30px', '32px', '34px', '36px',
        '40px', '44px', '48px', '56px', '64px', '72px', '80px', '96px',
        '0.625rem', '0.6875rem', '0.75rem', '0.8125rem', '0.875rem', '1rem',
        '1.125rem', '1.25rem', '1.375rem', '1.5rem', '1.75rem', '2rem',
        '2.25rem', '2.5rem', '3rem', '3.5rem', '4rem', '5rem', '6rem',
    ]

    def __init__(self, source: Optional[str] = None, output: Optional[str] = None,
                 format: str = 'css', url: Optional[str] = None):
        self.source = source
        self.output = output
        self.format = format
        self.url = url

    def _read_source(self) -> str:
        """Read source content from file or URL."""
        if self.url:
            try:
                with urlopen(self.url, timeout=10) as response:
                    return response.read().decode('utf-8', errors='ignore')
            except (URLError, Exception) as e:
                raise RuntimeError(f"Failed to fetch URL: {e}")
        elif self.source:
            path = Path(self.source)
            if not path.exists():
                raise FileNotFoundError(f"Source file not found: {self.source}")
            return path.read_text(encoding='utf-8')
        else:
            raise ValueError("Either --source or --url must be provided")

    def _detect_format(self, content: str) -> str:
        """Auto-detect source format."""
        if self.format != 'auto':
            return self.format
        if '<html' in content.lower() or '<!doctype' in content.lower():
            return 'html'
        if re.search(r'[.#][\w-]+\s*\{', content):
            return 'css'
        return 'css'

    def _extract_colors(self, content: str) -> List[Dict[str, Any]]:
        """Extract color values from content."""
        colors = []
        seen = set()

        for pattern in self.COLOR_PATTERNS:
            matches = re.findall(pattern, content)
            for match in matches:
                normalized = match.lower()
                if normalized not in seen:
                    seen.add(normalized)
                    colors.append({
                        "name": self._color_to_name(normalized),
                        "value": normalized,
                        "format": self._detect_color_format(normalized),
                        "description": f"Extracted color {normalized}",
                        "variants": {},
                        "usage": "auto-extracted",
                    })

        return colors

    def _color_to_name(self, color: str) -> str:
        """Generate a semantic name for a color value."""
        # Common color name mapping
        common_colors = {
            '#000000': 'black', '#ffffff': 'white',
            '#ff0000': 'red', '#00ff00': 'green', '#0000ff': 'blue',
            '#ffff00': 'yellow', '#ff00ff': 'magenta', '#00ffff': 'cyan',
            '#808080': 'gray', '#c0c0c0': 'silver',
            '#ff6b6b': 'danger', '#51cf66': 'success', '#339af0': 'info',
            '#fcc419': 'warning',
        }
        if color.lower() in common_colors:
            return common_colors[color.lower()]
        # Generate name from hex value
        clean = color.lstrip('#').lower()
        return f"color-{clean}"

    def _detect_color_format(self, color: str) -> str:
        """Detect color format type."""
        if color.startswith('#'):
            return 'hex'
        if color.startswith('rgb'):
            return 'rgb'
        if color.startswith('hsl'):
            return 'hsl'
        return 'named'

    def _extract_spacing(self, content: str) -> List[Dict[str, Any]]:
        """Extract spacing values from CSS properties."""
        spacing_props = re.findall(
            r'(?:margin|padding|gap|top|bottom|left|right)\s*:\s*([^;}{]+)',
            content, re.IGNORECASE
        )
        spacing_values = []
        seen = set()

        for prop_value in spacing_props:
            values = re.findall(r'(-?\d+(?:\.\d+)?(?:px|rem|em|%))', prop_value)
            for val in values:
                if val not in seen:
                    seen.add(val)
                    spacing_values.append({
                        "name": f"space-{val.replace('.', '-').replace('px', '').replace('rem', '-rem').replace('em', '-em')}",
                        "value": val,
                        "description": f"Spacing value {val}",
                        "usage": "auto-extracted",
                    })

        return spacing_values

    def _extract_typography(self, content: str) -> List[Dict[str, Any]]:
        """Extract typography tokens from CSS."""
        typography = []
        seen_fonts = set()

        # Extract font-family
        font_families = re.findall(
            r'font-family\s*:\s*([^;}{]+)',
            content, re.IGNORECASE
        )
        for ff in font_families:
            fonts = [f.strip().strip('\'"') for f in ff.split(',')]
            primary = fonts[0] if fonts else "sans-serif"
            if primary not in seen_fonts:
                seen_fonts.add(primary)
                typography.append({
                    "name": f"font-{primary.lower().replace(' ', '-')}",
                    "family": primary,
                    "size": "",
                    "weight": "",
                    "line_height": "",
                    "letter_spacing": "",
                    "description": f"Font family: {primary}",
                    "usage": "auto-extracted",
                })

        # Extract font-size
        font_sizes = re.findall(
            r'font-size\s*:\s*([^;}{]+)',
            content, re.IGNORECASE
        )
        seen_sizes = set()
        for fs in font_sizes:
            fs = fs.strip()
            if fs not in seen_sizes:
                seen_sizes.add(fs)
                typography.append({
                    "name": f"text-{fs.replace('.', '-').replace('px', '').replace('rem', '-rem')}",
                    "family": "",
                    "size": fs,
                    "weight": "",
                    "line_height": "",
                    "letter_spacing": "",
                    "description": f"Font size: {fs}",
                    "usage": "auto-extracted",
                })

        # Extract font-weight
        font_weights = re.findall(
            r'font-weight\s*:\s*(\w+)',
            content, re.IGNORECASE
        )
        seen_weights = set()
        for fw in font_weights:
            if fw not in seen_weights:
                seen_weights.add(fw)
                typography.append({
                    "name": f"weight-{fw}",
                    "family": "",
                    "size": "",
                    "weight": fw,
                    "line_height": "",
                    "letter_spacing": "",
                    "description": f"Font weight: {fw}",
                    "usage": "auto-extracted",
                })

        return typography

    def _extract_shadows(self, content: str) -> List[Dict[str, Any]]:
        """Extract box-shadow values."""
        shadows = re.findall(
            r'box-shadow\s*:\s*([^;}{]+)',
            content, re.IGNORECASE
        )
        result = []
        seen = set()
        for shadow in shadows:
            shadow = shadow.strip()
            if shadow and shadow not in seen:
                seen.add(shadow)
                result.append({
                    "name": f"shadow-{len(result) + 1}",
                    "value": shadow,
                    "description": f"Box shadow: {shadow[:60]}{'...' if len(shadow) > 60 else ''}",
                    "usage": "auto-extracted",
                })
        return result

    def _extract_border_radius(self, content: str) -> List[Dict[str, Any]]:
        """Extract border-radius values."""
        radii = re.findall(
            r'border-radius\s*:\s*([^;}{]+)',
            content, re.IGNORECASE
        )
        result = []
        seen = set()
        for radius in radii:
            radius = radius.strip()
            if radius and radius not in seen:
                seen.add(radius)
                result.append({
                    "name": f"radius-{radius.replace('.', '-').replace('px', '').replace('%', 'pct')}",
                    "value": radius,
                    "description": f"Border radius: {radius}",
                    "usage": "auto-extracted",
                })
        return result

    def _extract_breakpoints(self, content: str) -> List[Dict[str, Any]]:
        """Extract media query breakpoints."""
        queries = re.findall(
            r'@media\s*\([^)]*(?:min|max)-width\s*:\s*(\d+(?:\.\d+)?(?:px|rem|em))',
            content, re.IGNORECASE
        )
        result = []
        seen = set()
        for bp in queries:
            bp = bp.strip()
            if bp not in seen:
                seen.add(bp)
                result.append({
                    "name": f"breakpoint-{bp.replace('.', '-').replace('px', '').replace('rem', '-rem')}",
                    "value": bp,
                    "description": f"Breakpoint at {bp}",
                })
        return result

    def extract(self) -> Dict[str, Any]:
        """Perform full extraction and return token dictionary."""
        content = self._read_source()
        fmt = self._detect_format(content)

        print(f"🔍 Analyzing {fmt.upper()} content ({len(content)} chars)...")

        tokens = {
            "colors": self._extract_colors(content),
            "typography": self._extract_typography(content),
            "spacing": self._extract_spacing(content),
            "shadows": self._extract_shadows(content),
            "borderRadius": self._extract_border_radius(content),
            "breakpoints": self._extract_breakpoints(content),
        }

        total = sum(len(v) for v in tokens.values())
        print(f"📊 Found {total} tokens across {sum(1 for v in tokens.values() if v)} categories")

        return tokens
