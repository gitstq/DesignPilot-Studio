#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Design Token Models - Data structures for design system tokens
设计令牌数据模型

Defines the core data structures used throughout DesignPilot:
- ColorToken: Color definitions with variants
- TypographyToken: Font family, size, weight, line-height
- SpacingToken: Margin, padding, gap values
- ShadowToken: Box shadow definitions
- BorderRadiusToken: Border radius values
- DesignSystem: Complete design system container
"""

import json
import re
from dataclasses import dataclass, field, asdict
from typing import Optional, List, Dict, Any
from enum import Enum


class ColorFormat(Enum):
    """Supported color formats."""
    HEX = "hex"
    RGB = "rgb"
    HSL = "hsl"
    NAMED = "named"


@dataclass
class ColorToken:
    """Represents a color design token."""
    name: str
    value: str
    format: str = "hex"
    description: str = ""
    variants: Dict[str, str] = field(default_factory=dict)
    usage: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ColorToken":
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})

    def to_css_var(self) -> str:
        """Convert to CSS custom property."""
        var_name = re.sub(r'[^a-zA-Z0-9]', '-', self.name).lower()
        var_name = re.sub(r'-+', '-', var_name).strip('-')
        return f"  --color-{var_name}: {self.value};"


@dataclass
class TypographyToken:
    """Represents a typography design token."""
    name: str
    family: str = ""
    size: str = ""
    weight: str = ""
    line_height: str = ""
    letter_spacing: str = ""
    description: str = ""
    usage: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "TypographyToken":
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})

    def to_css_var(self) -> str:
        """Convert to CSS custom properties."""
        var_name = re.sub(r'[^a-zA-Z0-9]', '-', self.name).lower()
        var_name = re.sub(r'-+', '-', var_name).strip('-')
        lines = []
        if self.family:
            lines.append(f"  --font-{var_name}-family: {self.family};")
        if self.size:
            lines.append(f"  --font-{var_name}-size: {self.size};")
        if self.weight:
            lines.append(f"  --font-{var_name}-weight: {self.weight};")
        if self.line_height:
            lines.append(f"  --font-{var_name}-line-height: {self.line_height};")
        if self.letter_spacing:
            lines.append(f"  --font-{var_name}-letter-spacing: {self.letter_spacing};")
        return "\n".join(lines)


@dataclass
class SpacingToken:
    """Represents a spacing design token."""
    name: str
    value: str
    description: str = ""
    usage: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SpacingToken":
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})

    def to_css_var(self) -> str:
        """Convert to CSS custom property."""
        var_name = re.sub(r'[^a-zA-Z0-9]', '-', self.name).lower()
        var_name = re.sub(r'-+', '-', var_name).strip('-')
        return f"  --spacing-{var_name}: {self.value};"


@dataclass
class ShadowToken:
    """Represents a shadow design token."""
    name: str
    value: str
    description: str = ""
    usage: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ShadowToken":
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})

    def to_css_var(self) -> str:
        """Convert to CSS custom property."""
        var_name = re.sub(r'[^a-zA-Z0-9]', '-', self.name).lower()
        var_name = re.sub(r'-+', '-', var_name).strip('-')
        return f"  --shadow-{var_name}: {self.value};"


@dataclass
class BorderRadiusToken:
    """Represents a border radius design token."""
    name: str
    value: str
    description: str = ""
    usage: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BorderRadiusToken":
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})

    def to_css_var(self) -> str:
        """Convert to CSS custom property."""
        var_name = re.sub(r'[^a-zA-Z0-9]', '-', self.name).lower()
        var_name = re.sub(r'-+', '-', var_name).strip('-')
        return f"  --radius-{var_name}: {self.value};"


@dataclass
class BreakpointToken:
    """Represents a responsive breakpoint token."""
    name: str
    value: str
    description: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BreakpointToken":
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})

    def to_css_var(self) -> str:
        """Convert to CSS media query."""
        var_name = re.sub(r'[^a-zA-Z0-9]', '-', self.name).lower()
        var_name = re.sub(r'-+', '-', var_name).strip('-')
        return f"  --breakpoint-{var_name}: {self.value};"


@dataclass
class AnimationToken:
    """Represents an animation design token."""
    name: str
    duration: str = ""
    easing: str = ""
    description: str = ""
    usage: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AnimationToken":
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})

    def to_css_var(self) -> str:
        """Convert to CSS custom properties."""
        var_name = re.sub(r'[^a-zA-Z0-9]', '-', self.name).lower()
        var_name = re.sub(r'-+', '-', var_name).strip('-')
        lines = []
        if self.duration:
            lines.append(f"  --animation-{var_name}-duration: {self.duration};")
        if self.easing:
            lines.append(f"  --animation-{var_name}-easing: {self.easing};")
        return "\n".join(lines)


@dataclass
class DesignSystem:
    """Complete design system container."""
    name: str = ""
    version: str = "1.0.0"
    description: str = ""
    author: str = ""
    colors: List[ColorToken] = field(default_factory=list)
    typography: List[TypographyToken] = field(default_factory=list)
    spacing: List[SpacingToken] = field(default_factory=list)
    shadows: List[ShadowToken] = field(default_factory=list)
    border_radius: List[BorderRadiusToken] = field(default_factory=list)
    breakpoints: List[BreakpointToken] = field(default_factory=list)
    animations: List[AnimationToken] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Serialize design system to dictionary."""
        data = {
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "author": self.author,
            "tokens": {
                "colors": [c.to_dict() for c in self.colors],
                "typography": [t.to_dict() for t in self.typography],
                "spacing": [s.to_dict() for s in self.spacing],
                "shadows": [s.to_dict() for s in self.shadows],
                "borderRadius": [b.to_dict() for b in self.border_radius],
                "breakpoints": [b.to_dict() for b in self.breakpoints],
                "animations": [a.to_dict() for a in self.animations],
            },
            "metadata": self.metadata,
        }
        return data

    def to_json(self, indent: int = 2) -> str:
        """Serialize to JSON string."""
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DesignSystem":
        """Deserialize from dictionary."""
        tokens = data.get("tokens", {})
        return cls(
            name=data.get("name", ""),
            version=data.get("version", "1.0.0"),
            description=data.get("description", ""),
            author=data.get("author", ""),
            colors=[ColorToken.from_dict(c) for c in tokens.get("colors", [])],
            typography=[TypographyToken.from_dict(t) for t in tokens.get("typography", [])],
            spacing=[SpacingToken.from_dict(s) for s in tokens.get("spacing", [])],
            shadows=[ShadowToken.from_dict(s) for s in tokens.get("shadows", [])],
            border_radius=[BorderRadiusToken.from_dict(b) for b in tokens.get("borderRadius", [])],
            breakpoints=[BreakpointToken.from_dict(b) for b in tokens.get("breakpoints", [])],
            animations=[AnimationToken.from_dict(a) for a in tokens.get("animations", [])],
            metadata=data.get("metadata", {}),
        )

    @classmethod
    def from_json(cls, json_str: str) -> "DesignSystem":
        """Deserialize from JSON string."""
        return cls.from_dict(json.loads(json_str))

    @classmethod
    def from_json_file(cls, file_path: str) -> "DesignSystem":
        """Deserialize from JSON file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            return cls.from_dict(json.load(f))

    def token_count(self) -> int:
        """Total number of tokens."""
        return (len(self.colors) + len(self.typography) + len(self.spacing) +
                len(self.shadows) + len(self.border_radius) +
                len(self.breakpoints) + len(self.animations))

    def summary(self) -> str:
        """Generate a summary string."""
        return (
            f"Design System: {self.name} v{self.version}\n"
            f"  Colors: {len(self.colors)}\n"
            f"  Typography: {len(self.typography)}\n"
            f"  Spacing: {len(self.spacing)}\n"
            f"  Shadows: {len(self.shadows)}\n"
            f"  Border Radius: {len(self.border_radius)}\n"
            f"  Breakpoints: {len(self.breakpoints)}\n"
            f"  Animations: {len(self.animations)}\n"
            f"  Total: {self.token_count()} tokens"
        )
